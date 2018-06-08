# -*- coding: utf-8 -*-
import os
import httplib2

from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect,HttpResponseServerError  
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv

from django.core.urlresolvers import reverse
from threading import Timer

from main.forms import *
from main.email import *
from db.forms import *
from db.models import Edificacion, Comunidad, Comentario, Etapa, InformeSemestral, InformeSemestralPublico
from usuarios.models import Usuario

from django.contrib.formtools.wizard.forms import ManagementForm
from collections import OrderedDict

import StringIO
import zipfile

import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string


import logging

from apiclient.discovery import build
from django.http import HttpResponseBadRequest

from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

from datetime import timedelta
from datetime import datetime
import datetime
import time

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(settings.BASE_DIR,'client_secret_661085975402-3iiorol92djh7n2fgo8ic9lsmuf8iffn.apps.googleusercontent.com.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/calendar',
    #redirect_uri='http://127.0.0.1:8000/oauth2callback')
    redirect_uri='http://proyectos.laalianzacristiana.co/oauth2callback')

def home(request):

    if request.user.is_authenticated():
        
        if request.user.tipo == Usuario.NACIONAL:
            return redirect('home_nacional')

        if request.user.tipo == Usuario.REGIONAL:
            return redirect('home_regional')

        if request.user.tipo == Usuario.LOCAL:
            return redirect('home_local')

        if request.user.tipo == Usuario.ARQUITECTO:
            return redirect('home_otros')

        if request.user.tipo == Usuario.INGENIERO:
            return redirect('home_otros')

        if request.user.tipo == Usuario.TESORERO:
            return redirect('home_otros')
        
    return redirect('hacer_login')


@login_required
def home_nacional(request, etapa=None):
    
    # validamos que el usuario tenga permiso de ver esta vista
    if request.user.tipo != Usuario.NACIONAL:
        raise PermissionDenied 
    
    proyectos = None
    ctx = {}
    
    if etapa:
        proyectos = Edificacion.objects.filter(etapa_actual=etapa)  
        ctx['etapa_actual'] = int(etapa) 
    else:
        proyectos = Edificacion.objects.all()
    
    
    ctx['proyectos'] = proyectos
    return render(request, 'main/home-nacional.html', ctx)



@login_required
def home_nacional_region(request, region=None):
    
    # validamos que el usuario tenga permiso de ver esta vista
    if request.user.tipo != Usuario.NACIONAL:
        raise PermissionDenied 
    
    proyectos = None
    ctx = {}
    
    if region:
        proyectos = Edificacion.objects.filter(congregacion__region=region)       
        ctx['region_actual'] = int(region) 
    else:
        proyectos = Edificacion.objects.all()
    
    
    ctx['proyectos'] = proyectos
    return render(request, 'main/home-nacional.html', ctx)


@login_required
def home_regional(request):

    # validamos que el usuario tenga permiso de ver esta vista
    if request.user.tipo != Usuario.REGIONAL:
        raise PermissionDenied 
    # Obtengo los usuarios que son hijos del regional
    users_hijos = Usuario.objects.filter(user_padre__exact=request.user.pk).values('pk')
    proyectos = Edificacion.objects.filter(usuario__in=users_hijos)

    ctx = {'proyectos': proyectos}
    return render(request, 'main/home-regional.html', ctx)


@login_required
def home_local(request):
    # validamos que el usuario tenga permiso de ver esta vista
    if request.user.tipo != Usuario.LOCAL:
        raise PermissionDenied 

    proyectos = Edificacion.objects.filter(usuario__exact=request.user.pk)
    ctx = {'proyectos': proyectos}
    return render(request, 'main/home-local.html', ctx)


@login_required
def home_otros(request, etapa=None):
    # validamos que el usuario tenga permiso de ver esta vista
    users = [Usuario.LOCAL, Usuario.REGIONAL, Usuario.NACIONAL]
    if request.user.tipo in users:
        raise PermissionDenied 

    ctx = {}          
    proyectos = None   
 
    if etapa:       
        if request.user.tipo == Usuario.ARQUITECTO: 
            proyectos = Edificacion.objects.filter(arquitecto__exact=request.user.pk,etapa_actual=etapa)
        if request.user.tipo == Usuario.INGENIERO:
            proyectos = Edificacion.objects.filter(ingeniero__exact=request.user.pk,etapa_actual=etapa)
        if request.user.tipo == Usuario.TESORERO:
            proyectos = Edificacion.objects.filter(tesorero__exact=request.user.pk,etapa_actual=etapa) 
        ctx['etapa_actual'] = int(etapa) 
    else:   
        if request.user.tipo == Usuario.ARQUITECTO: 
            proyectos = Edificacion.objects.filter(arquitecto__exact=request.user.pk)
        if request.user.tipo == Usuario.INGENIERO:
            proyectos = Edificacion.objects.filter(ingeniero__exact=request.user.pk)
        if request.user.tipo == Usuario.TESORERO:
            proyectos = Edificacion.objects.filter(tesorero__exact=request.user.pk)

    ctx['proyectos'] = proyectos
    return render(request, 'main/home-otros.html', ctx)

@login_required
def home_otros_region(request, region=None):
    
    # validamos que el usuario tenga permiso de ver esta vista
    if request.user.tipo != Usuario.ARQUITECTO and request.user.tipo != Usuario.TESORERO and request.user.tipo != Usuario.INGENIERO:
        raise PermissionDenied 

    proyectos = None
    ctx = {}

    if region:       
        if request.user.tipo == Usuario.ARQUITECTO: 
            proyectos = Edificacion.objects.filter(arquitecto__exact=request.user.pk,congregacion__region=region)
        if request.user.tipo == Usuario.INGENIERO:
            proyectos = Edificacion.objects.filter(ingeniero__exact=request.user.pk,congregacion__region=region)
        if request.user.tipo == Usuario.TESORERO:
            proyectos = Edificacion.objects.filter(tesorero__exact=request.user.pk,congregacion__region=region) 
        ctx['region_actual'] = int(region) 
    else:
        if request.user.tipo == Usuario.ARQUITECTO: 
            proyectos = Edificacion.objects.filter(arquitecto__exact=request.user.pk)
        if request.user.tipo == Usuario.INGENIERO:
            proyectos = Edificacion.objects.filter(ingeniero__exact=request.user.pk)
        if request.user.tipo == Usuario.TESORERO:
            proyectos = Edificacion.objects.filter(tesorero__exact=request.user.pk) 
        
    ctx['proyectos'] = proyectos
    return render(request, 'main/home-otros.html', ctx)

form_list = [EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, AdjuntosForm, CondicionesForm]

@login_required
def proyecto_nuevo(request):

    #restriccion vertical
    if request.user.tipo != Usuario.LOCAL:
        raise PermissionDenied
 
    form = EdificacionForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            edificacion = form.save(commit=False)
            edificacion.usuario = request.user

            edificacion.estado       = form_list.index(form.__class__) # obtenemos un valor compatible con los elementos de la lista
            edificacion.usuario      = request.user
            edificacion.etapa_actual = Etapa.DILIGENCIAMIENTO   
            edificacion.save()
            
            #Registramos la etapa de Diligenciamiento
            registrar_etapa(edificacion, Etapa.DILIGENCIAMIENTO)

            return redirect(reverse('proyecto_edit', args=[edificacion.pk, 1]))  # redireccionamos al segundo formulario en modo edit
     
    ctx = {'form': form, 'form_list': form_list, 'paso':1}

    return render(request, 'main/proyecto-forms.html', ctx)


@login_required
def proyecto_edit(request, pk, form_index):

    proyecto  =  get_object_or_404(Edificacion, pk=pk)

    """ validaciones """
    
    if request.user.tipo != Usuario.LOCAL or request.user.pk != proyecto.usuario.pk:    #restriccion vertical, solo locales entran aqui
        raise PermissionDenied                                                          #restirccion horizontal, no puede ver el proyecto de otro 

    if int(form_index) > proyecto.estado + 1: # validamos que el usuario cree los formularios en orden
        raise PermissionDenied 


    """ preparamos el form a enviar o a guardar """

    form_class = form_list[int(form_index)]

    if int(form_index) == 0:   # si es el primer formulario siempre habra un modelo porque lo validamos arriba
        instance = proyecto or None
           
    else:
        try:
            instance = form_class.Meta.model.objects.get(edificacion=pk)   # verificamos en la db si el objeto existe para pasarlo como instancia
        except form_class.Meta.model.DoesNotExist:
            instance = None

    form = form_class(request.POST or None, request.FILES or None, instance=instance)


    """ manejamos el envio del formulario """
    
    if request.method == 'POST':
        
        if form.is_valid():

            model_obj = form.save(commit=False)
            
            if model_obj.pk is None: # si es nuevo hacemos operaciones adicionales
                model_obj.edificacion = proyecto
                model_obj.save()

                proyecto.estado = int(form_index)
                proyecto.save(update_fields=['estado'])

                # aqui verifico que sea el ultimo que hace cambiar de etapa y envia la aplicion completa redirecionando al done
                if int(form_index) == (len(form_list) - 1):
                    
                    registrar_etapa(proyecto, Etapa.APROB_REGIONAL)
                    mail_change_etapa(proyecto, self.request.user)

                    return redirect(reverse('done', args=[proyecto.pk])) # redireccionamos al done 


            elif model_obj.pk:   # explicito para mayor seguridad al leer
                model_obj.save() # si no es nuevo simplemente los guardamos
                if int(form_index) == (len(form_list) - 1):
                    return redirect(proyecto) # redireccionamos a vista detalle

                
            return redirect(reverse('proyecto_edit', args=[proyecto.pk, int(form_index)+1]))  # redirigimos al siguiente si no es el ultimo


    ctx = {'form': form, 'form_list': form_list, 'proyecto':proyecto, 'paso':int(form_index)+1}

    return render(request, 'main/proyecto-forms.html', ctx)


@login_required
def proyecto_zip(request, pk):

    proyecto  =  get_object_or_404(Edificacion, pk=pk)

    """ validaciones """
    
    if request.user.tipo == Usuario.LOCAL and request.user.pk != proyecto.usuario.pk:    #restriccion vertical, solo locales entran aqui
        raise PermissionDenied                                                          #restirccion horizontal, no puede ver el proyecto de otro 

    # OJO VALIDAR QUE EN CREACION NO SE PUEDA SALTAR EL ORDEN ESTRICTO DE FORMULARIOS
    adjuntos =  Adjuntos.objects.get(edificacion=proyecto)
    filenames = []  
    if adjuntos.foto_construccion:        
        filenames += [adjuntos.foto_construccion.path]
    if adjuntos.foto_congregacion:
        filenames += [adjuntos.foto_congregacion.path]
    if adjuntos.foto_pastor:
        filenames += [adjuntos.foto_pastor.path]
    if adjuntos.permiso_construccion: 
        filenames += [adjuntos.permiso_construccion.path]
    if adjuntos.escritura_terreno:   
        filenames += [adjuntos.escritura_terreno.path]
    if adjuntos.manzana_catastral:    
        filenames += [adjuntos.manzana_catastral.path]
    if adjuntos.plan_construccion:    
        filenames += [adjuntos.plan_construccion.path]
    if adjuntos.certificacion:
        if adjuntos.certificacion != 'ninguno':  #validamos que el valor sea diferente de ninguno
            print "Certificacioin pasa"
            filenames += [adjuntos.certificacion.path]    
    if adjuntos.historia_congregacion:    
        filenames += [adjuntos.historia_congregacion.path]    
    if adjuntos.testimonio_pastor:    
        filenames += [adjuntos.testimonio_pastor.path]    
    if adjuntos.planos_arquitecto:    
        filenames += [adjuntos.planos_arquitecto.path]                

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "Comprimido"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO.StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type = "application/zip")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp


def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse 
    links    = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result,link_callback=links)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

@login_required
def proyecto_pdf(request, pk):

    proyecto  =  get_object_or_404(Edificacion, pk=pk)
    comentarios  = Comentario.objects.filter(edificacion=proyecto).order_by('-created')

    if request.user.tipo == Usuario.LOCAL and request.user.pk != proyecto.usuario.pk:    #restriccion vertical, solo locales entran aqui
        raise PermissionDenied  
    
    ctx = {'pagesize':'A4' , 'proyecto': proyecto , 'comentarios': comentarios }        

    try:
        comunidad =  Comunidad.objects.get(edificacion=proyecto)
        ctx['comunidad'] = comunidad
    except Comunidad.DoesNotExist:
        pass

    try:
        congregacion =  Congregacion.objects.get(edificacion=proyecto)
        ctx['congregacion'] = congregacion
    except Congregacion.DoesNotExist:
        pass
        
    try:
        adjuntos =  Adjuntos.objects.get(edificacion=proyecto)
        ctx['adjuntos'] = adjuntos        
    except Adjuntos.DoesNotExist:
        pass   

    try:
        financiera =  InformacionFinanciera.objects.get(edificacion=proyecto)
        ctx['financiera'] = financiera
    except InformacionFinanciera.DoesNotExist:
        pass    

    try:
        condiciones =  Condiciones.objects.get(edificacion=proyecto)
        ctx['condiciones'] = condiciones
    except Condiciones.DoesNotExist:
        pass   
       
    html = render_to_string('main/pdf.html',ctx, context_instance=RequestContext(request))
    return generar_pdf(html)


@login_required
def informe_pdf(request, pk, index):

    proyecto  =  get_object_or_404(Edificacion, pk=pk)    

    if request.user.tipo != Usuario.NACIONAL :    #restriccion vertical, solo locales entran aqui
        raise PermissionDenied  
    
    ctx = { 'pagesize':'A4' , 'proyecto': proyecto }      
    print index
    try:
        informe = InformeSemestral.objects.filter(edificacion=pk,informe=index)
        print informe[0]
        ctx['informe'] = informe[0]
    except InformeSemestral.DoesNotExist:
        pass

    html = render_to_string('main/pdf_informe.html',ctx, context_instance=RequestContext(request))
    return generar_pdf(html)

@login_required
def proyecto(request, pk):
    # validamos que el proyecto exista
    #[EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, AdjuntosForm, CondicionesForm]
    proyecto  =  get_object_or_404(Edificacion, pk=pk)
   
    # validamos que el usuario tenga permiso de ver el proyecto
    if request.user.tipo == Usuario.LOCAL and request.user.pk != proyecto.usuario.pk:
        raise PermissionDenied 
    
    form_informe_semestral = InformeSemestralForm()

    if request.method == 'POST':  
        if request.POST.get('miembros_actuales') == None:              
            form = ComentarioForm(request.POST)
            if form.is_valid():
                new_coment = form.save(commit=False)
                new_coment.edificacion = proyecto
                new_coment.commenter = request.user
                new_coment.save()

                result_email = mail_comentario(new_coment, proyecto)
                # redirect funciona con el objeto si en el existe el metodo get_absolute_url
                return redirect(proyecto)
        else:            
            form_informe_semestral = InformeSemestralForm(request.POST, request.FILES)       
            if form_informe_semestral.is_valid():
                try:
                    informes = InformeSemestral.objects.filter(edificacion=pk)       
                    numero_inf = len(informes) + 1
                except InformeSemestral.DoesNotExist:
                    numero_inf = 1
                informeObject = form_informe_semestral.save(commit=False)     
                informeObject.informe = numero_inf
                informeObject.edificacion = proyecto
                informeObject.save()                         
                return redirect(proyecto)            
            
    comentarios  = Comentario.objects.filter(edificacion=pk).order_by('-created')
    comentarioForm         = ComentarioForm()
    comentarioForm.helper.form_action = proyecto.get_absolute_url()

    ctx = {'proyecto': proyecto, 'Etapa': Etapa, 'comentarios': comentarios, 'comentarioForm': comentarioForm}
    ctx['aprobacionForm'] = AprobacionForm()  

    #PRUEBA DE EMAIL CON ESTILO
    #mail_prueba()
  
    try:
        comunidad =  Comunidad.objects.get(edificacion=proyecto)
        ctx['comunidad'] = comunidad
    except Comunidad.DoesNotExist:
        pass

    try:
        congregacion =  Congregacion.objects.get(edificacion=proyecto)
        ctx['congregacion'] = congregacion
    except Congregacion.DoesNotExist:
        pass
        
    try:
        adjuntos =  Adjuntos.objects.get(edificacion=proyecto)
        ctx['adjuntos'] = adjuntos     

        adj = proyecto.adjuntos_set.get()
        if proyecto.etapa_actual == Etapa.CONS_P1:            
            ctx['FotosPAForm'] = FotosPAForm(instance=adj)
        elif proyecto.etapa_actual == Etapa.CONS_P2: 
           ctx['FotosPBForm'] = FotosPBForm(instance=adj)
        elif proyecto.etapa_actual == Etapa.CONS_P3: 
           ctx['FotosPCForm'] = FotosPCForm(instance=adj)
        elif proyecto.etapa_actual == Etapa.DEDICACION: 
           ctx['DedicacionForm'] = DedicacionForm(instance=adj)

    except Adjuntos.DoesNotExist:
        pass   

    try:
        financiera =  InformacionFinanciera.objects.get(edificacion=proyecto)
        ctx['financiera'] = financiera
    except InformacionFinanciera.DoesNotExist:
        pass    

    try:
        condiciones =  Condiciones.objects.get(edificacion=proyecto)
        ctx['condiciones'] = condiciones
    except Condiciones.DoesNotExist:
        pass
    
    #Solo si esta despues de la dedicatione
    if proyecto.etapa_actual >= Etapa.DEDICACION:        
        try:        
            #0 -> No lo  ha lleano, 1--> Amarilio - Espera que sea la fecha  2 --> Verde full
            informes = InformeSemestral.objects.filter(edificacion=pk)                        
            ctx['informes'] = informes
            print informes
            if len(informes) <= 6 and len(informes) > 0:
                pre_inform = informes[len(informes)-1].fecha_elaboracion
                if pre_inform.month <= 6:
                   rango = 'Julio - Diciembre del '+str(pre_inform.year)
                   fecha_ini = datetime.datetime.strptime("01 07 "+str(pre_inform.year), '%d %m %Y').date()
                else:
                   rango = 'Enero - Junio del '+str(pre_inform.year+1)
                   fecha_ini = datetime.datetime.strptime("01 01 "+str(pre_inform.year+1), '%d %m %Y').date()

                if date.today() > fecha_ini:
                    ctx['informes_status'] = 0
                else:
                    ctx['informes_status'] = 1
                 
                ctx['informeForm'] = form_informe_semestral          
                ctx['informes_texto'] = "Informe desde "+rango
            elif len(informes) == 0:
                raise InformeSemestral.DoesNotExist
            else:  
                ctx['informes_status'] = 2 
                ctx['informeForm'] = form_informe_semestral            

        except InformeSemestral.DoesNotExist:
            ctx['informes_status'] = 0         
            dedicatione = proyecto.fecha_aprox_dedicacion
            if dedicatione.month <= 6:
               rango = 'Julio - Diciembre del '+str(dedicatione.year)
            else:
               rango = 'Enero - Junio del '+str(dedicatione.year+1) 
            ctx['informeForm'] = form_informe_semestral            
            ctx['informes_texto'] = "Informe desde "+rango
            pass

    if request.user.tipo == Usuario.ARQUITECTO:
        adj = proyecto.adjuntos_set.get()
        ctx['planosArquitectoForm'] = PlanosArquitectoForm(instance=adj)

    if request.user.tipo == Usuario.INGENIERO: 
        adj = proyecto.adjuntos_set.get()
        ctx['planosIngenieroForm'] = PlanosIngenieroForm(instance=adj) 

    if request.user.tipo == Usuario.TESORERO:
        ctx['aprobacionTesoreroForm'] = AprobacionTesoreroForm(instance=proyecto) 
    
    if request.user.tipo == Usuario.NACIONAL:
        ctx['aprobacionNacionalForm'] = AprobacionNacionalForm(instance=proyecto) 
        
        asignarUsuariosForm = AsignarUsuariosForm(instance=proyecto)
        asignarUsuariosForm.helper.form_action = reverse('asignaciones', args=[proyecto.pk])
        ctx['asignarUsuariosForm'] = asignarUsuariosForm

        arquitectoEditForm = ArquitectoEditForm(instance=proyecto)
        arquitectoEditForm.helper.form_action = reverse('asignaciones', args=[proyecto.pk])
        ctx['arquitectoEditForm'] = arquitectoEditForm
        
        ingenieroEditForm = IngenieroEditForm(instance=proyecto)
        ingenieroEditForm.helper.form_action = reverse('asignaciones', args=[proyecto.pk])
        ctx['ingenieroEditForm'] = ingenieroEditForm

        tesoreroEditForm = TesoreroEditForm(instance=proyecto)
        tesoreroEditForm.helper.form_action = reverse('asignaciones', args=[proyecto.pk])
        ctx['tesoreroEditForm'] = tesoreroEditForm

        asignarICMPinForm = AsignarICMPinForm(instance=proyecto)
        asignarICMPinForm.helper.form_action = reverse('asignar_pin', args=[proyecto.pk])
        ctx['icmPinForm'] = asignarICMPinForm
        
    
    return render(request, 'main/proyecto.html', ctx)


def registrar_etapa(edificacion, etapa):
    _etapa = Etapa(edificacion=edificacion, etapa=etapa)
    _etapa.save()

@login_required
def autorizaciones(request, pk):

    if request.method == 'POST':
        proyecto  =  get_object_or_404(Edificacion, pk=pk)   

        if request.user.tipo == Usuario.REGIONAL:

            if proyecto.etapa_actual == Etapa.APROB_REGIONAL and 'aprobar' in request.POST:   # validar y validar tanto aqui como en plantilla
                proyecto.aprobacion_regional = request.POST['aprobar']
                proyecto.save(update_fields=['aprobacion_regional'])    # el campo etapa_actual se actualiza en el modelo Etapa
                
                registrar_etapa(proyecto, Etapa.ASIGN_USUARIOS)  
                mail_change_etapa(proyecto, request.user)
        

        if request.user.tipo == Usuario.NACIONAL: 
            
            ##registrar_etapa(proyecto, Etapa.INFORMES)
            ##return redirect(proyecto)

            if proyecto.etapa_actual == Etapa.ASIGN_USUARIOS and 'aprobar' in request.POST:
                proyecto.usuarios_asignados = request.POST['aprobar']
                proyecto.save(update_fields=['usuarios_asignados'])

                registrar_etapa(proyecto, Etapa.PLANOS)
                mail_change_etapa(proyecto, request.user)

            elif proyecto.etapa_actual == Etapa.APROB_NACIONAL and 'aprobar' in request.POST:
                proyecto.aprobacion_nacional = request.POST['aprobar']
                proyecto.save(update_fields=['aprobacion_nacional'])

                registrar_etapa(proyecto, Etapa.APROB_INTERNACIONAL)
                mail_change_etapa(proyecto, request.user)

            elif proyecto.etapa_actual == Etapa.APROB_INTERNACIONAL and 'aprobar' in request.POST:
                proyecto.aprobacion_internacional = request.POST['aprobar']
                proyecto.save(update_fields=['aprobacion_internacional'])

                registrar_etapa(proyecto, Etapa.ESPERANDO_RECURSOS)
                mail_change_etapa(proyecto, request.user)    

            elif proyecto.etapa_actual == Etapa.ESPERANDO_RECURSOS and 'aprobar' in request.POST:       

                proyecto.envio_icm = request.POST['aprobar']
                proyecto.save(update_fields=['envio_icm'])

                proyecto.envio_alianza = False
                proyecto.save(update_fields=['envio_alianza'])         

                registrar_etapa(proyecto, Etapa.CONS_P1)                

                #Calculo la fecha de dedicacion aproximada para guardarla en la base de datos y notificar.
                #fecha_aprox_dedicacion
                etapa_inical_cons =  Etapa.objects.get(edificacion=proyecto,etapa=Etapa.CONS_P1)                 
                construction_final = etapa_inical_cons.created
                
                for key,value in Etapa.ETAPA_ACTUAL:
                  if key > Etapa.ESPERANDO_RECURSOS and key <= Etapa.DEDICACION:
                     if proyecto.tipo_construccion >= 2 and key == Etapa.CONS_P1: #Le añado 8 dias aprox del giro Alianza Iglesia
                        construction_final = construction_final+timedelta(days=68)
                     else:
                        construction_final = construction_final+timedelta(days=48)                       

                proyecto.fecha_aprox_dedicacion = construction_final
                proyecto.save(update_fields=['fecha_aprox_dedicacion'])

                mail_change_etapa(proyecto, request.user)                                             
                

            elif proyecto.etapa_actual == Etapa.CONS_P1 or proyecto.etapa_actual == Etapa.CONS_P2 or proyecto.etapa_actual == Etapa.CONS_P3 or proyecto.etapa_actual == Etapa.DEDICACION and 'aprobar' in request.POST:       
                
                if not proyecto.envio_icm:
                    #GIRO DE ICM
                    proyecto.envio_icm = request.POST['aprobar']
                    proyecto.save(update_fields=['envio_icm'])                
                    mail_change_sub_etapa(proyecto, request.user, "ICM envia fondos a la Alianza")                          
                elif proyecto.aprobacion_fotos == 1:
                    #APROBACION DE FOTOS
                    if proyecto.etapa_actual == Etapa.DEDICACION and proyecto.aprobacion_fotos != 2: #Fin de la etapa de Dedicacion
                       proyecto.aprobacion_fotos = 2
                       proyecto.save(update_fields=['aprobacion_fotos']) ##Aca seguiria a etapa de Infome 6 Mestral
                       #registrar_etapa(proyecto, Etapa.INFORMES) ##Pasamos a la etapada de Informes semestrales                                       
                    else:                        
                        proyecto.envio_icm = False
                        proyecto.save(update_fields=['envio_icm'])

                        proyecto.envio_alianza = False
                        proyecto.save(update_fields=['envio_alianza']) 

                        proyecto.aprobacion_fotos = 0
                        proyecto.save(update_fields=['aprobacion_fotos'])

                        if proyecto.etapa_actual == Etapa.CONS_P1:
                            registrar_etapa(proyecto, Etapa.CONS_P2)
                        else:                            
                            if proyecto.tipo_construccion >= 2 and proyecto.etapa_actual == Etapa.CONS_P2:
                                registrar_etapa(proyecto, Etapa.CONS_P3)                   
                            else:    
                                registrar_etapa(proyecto, Etapa.DEDICACION)   

                        mail_change_etapa(proyecto, request.user)

                elif proyecto.etapa_actual == Etapa.DEDICACION and proyecto.aprobacion_fotos == 2:
                    registrar_etapa(proyecto, Etapa.INFORMES)
                    mail_change_etapa(proyecto, request.user)        
                    
        if request.user.tipo == Usuario.ARQUITECTO or request.user.tipo == Usuario.INGENIERO:
            
            if proyecto.etapa_actual == Etapa.PLANOS and 'aprobar' in request.POST:
                
                if request.user.tipo == Usuario.ARQUITECTO:
                    proyecto.aprobacion_arquitecto = request.POST['aprobar']
                    proyecto.save(update_fields=['aprobacion_arquitecto'])

                if request.user.tipo == Usuario.INGENIERO:
                    proyecto.aprobacion_ingeniero = request.POST['aprobar']
                    proyecto.save(update_fields=['aprobacion_ingeniero'])

                if proyecto.arquitecto and proyecto.ingeniero: # si existen los dos usuarios
                    if proyecto.aprobacion_arquitecto and proyecto.aprobacion_ingeniero: # y solo si los dos han aprobado
                        if proyecto.tesorero:
                            registrar_etapa(proyecto, Etapa.APROB_TESORERO) # si hay tesorero vamos a esa etapa
                        else:
                            registrar_etapa(proyecto, Etapa.APROB_NACIONAL) # sino hay tesorero saltamos a la siguiente
                    
                        mail_change_etapa(proyecto, request.user)  # notificamos por email

                elif proyecto.arquitecto:
                    if proyecto.aprobacion_arquitecto and proyecto.tesorero:
                        registrar_etapa(proyecto, Etapa.APROB_TESORERO)
                    elif proyecto.aprobacion_arquitecto and not proyecto.tesorero:
                        registrar_etapa(proyecto, Etapa.APROB_NACIONAL)

                    mail_change_etapa(proyecto, request.user)  # notificamos por email

                elif proyecto.ingeniero:
                    if proyecto.aprobacion_ingeniero and proyecto.tesorero:
                        registrar_etapa(proyecto, Etapa.APROB_TESORERO)
                    elif proyecto.aprobacion_ingeniero and not proyecto.tesorero:
                        registrar_etapa(proyecto, Etapa.APROB_NACIONAL)

                    mail_change_etapa(proyecto, request.user)  # notificamos por email
           

        if request.user.tipo == Usuario.TESORERO:

            if proyecto.etapa_actual == Etapa.APROB_TESORERO and 'aprobar' in request.POST:   # validar y validar tanto aqui como en plantilla
                proyecto.aprobacion_tesorero = request.POST['aprobar']
                proyecto.save(update_fields=['aprobacion_tesorero'])    # el campo etapa_actual se actualiza en el modelo Etapa
                
                registrar_etapa(proyecto, Etapa.APROB_NACIONAL)  
                mail_change_etapa(proyecto, request.user)

            elif proyecto.etapa_actual == Etapa.CONS_P1 or proyecto.etapa_actual == Etapa.CONS_P2 or proyecto.etapa_actual == Etapa.CONS_P3 or proyecto.etapa_actual == Etapa.DEDICACION and 'aprobar' in request.POST:    
                if not proyecto.envio_alianza:
                    #GIRO ALIANZA
                    proyecto.envio_alianza = request.POST['aprobar']
                    proyecto.save(update_fields=['envio_alianza'])                  
                    mail_change_sub_etapa(proyecto, request.user, "Alianza envia fondos a la Iglesia Local")         

        return redirect(proyecto)

    raise Http404 

@login_required
def asignaciones(request, pk):
    """ 
    Metodo encargado de procesar las asignaciones de usuarios
    Arquitecto, Ingeniero y Tesorero en un proyecto
    """
    if request.method == 'POST':

        proyecto  =  get_object_or_404(Edificacion, pk=pk)

        if not 'editar' in request.POST:
            form = AsignarUsuariosForm(request.POST, instance=proyecto)
            form.save()
        
        elif request.POST['editar'] == Usuario.ARQUITECTO:
            form = ArquitectoEditForm(request.POST, instance=proyecto)
            form.save()

        elif request.POST['editar'] == Usuario.INGENIERO:
            form = IngenieroEditForm(request.POST, instance=proyecto)
            form.save()

        elif request.POST['editar'] == Usuario.TESORERO:
            form = TesoreroEditForm(request.POST, instance=proyecto)
            form.save()

        return redirect(proyecto)

    raise Http404

@login_required   # solo usuarios logueados
def asignar_pin(request, pk):
    if request.method == 'POST':  # solo llamadas post
        if request.user.tipo == Usuario.NACIONAL:  # solo usuario nacional
            proyecto  =  get_object_or_404(Edificacion, pk=pk)
            form = AsignarICMPinForm(request.POST, instance=proyecto)
            proj = form.save(commit=False)
            proj.save(update_fields=['icm_pin'])   # solo actualizar campo especifico
            return redirect(proyecto)
    
    raise Http404



@login_required
def planos(request, pk):
    if request.method == 'POST':
        proyecto  =  get_object_or_404(Edificacion, pk=pk)
        adjuntos  = proyecto.adjuntos_set.get()

        if request.POST['planos'] == Usuario.ARQUITECTO:
            form = PlanosArquitectoForm(request.POST, request.FILES, instance=adjuntos)
            form.save()

        if request.POST['planos'] == Usuario.INGENIERO:
            form = PlanosIngenieroForm(request.POST, request.FILES, instance=adjuntos)
            form.save()

        return redirect(proyecto)
    raise Http404  

@login_required
def dedicacion(request, pk):
    if request.method == 'POST':
        if request.user.tipo != Usuario.NACIONAL:
            raise PermissionDenied 
        proyecto  =  get_object_or_404(Edificacion, pk=pk)       
        try:                        
            proyecto.fecha_aprox_dedicacion = datetime.datetime.strptime(request.POST['fecha'], "%Y-%m-%d") #Careful fecha string 
            proyecto.save(update_fields=['fecha_aprox_dedicacion'])
            return redirect(proyecto)
        except:  
            raise Exception('Error procesando la fecha! '+request.POST['fecha'])  
    raise Http404  

@login_required
def fotos(request, pk):
    if request.method == 'POST':
        proyecto  =  get_object_or_404(Edificacion, pk=pk)
        adjuntos  = proyecto.adjuntos_set.get()
        
        if proyecto.etapa_actual == Etapa.CONS_P1:  
            if request.FILES['fotos_p1'].name.split('.')[-1] == "zip" or request.FILES['fotos_p1'].name.split('.')[-1] == "rar":   
                form = FotosPAForm(request.POST, request.FILES, instance=adjuntos)  
                form.save()  
                proyecto.aprobacion_fotos = 1 #Mean que esta en espera de aprobacion las fotos
                proyecto.save(update_fields=['aprobacion_fotos'])
            else:
                ctx = {'er': 'Recuerde que solo puede adjuntar archivos comprimidos Zip o Rar, el archivo debe contener las fotos de la Etapa actual de construccion para ser Revisadas por la Oficina Nacional', 'proyecto':proyecto}
                return render(request, 'main/error.html', ctx)            
        elif proyecto.etapa_actual == Etapa.CONS_P2:
            if request.FILES['fotos_p2'].name.split('.')[-1] == "zip" or request.FILES['fotos_p2'].name.split('.')[-1] == "rar":   
                form = FotosPBForm(request.POST, request.FILES, instance=adjuntos)
                form.save()                
                proyecto.aprobacion_fotos = 1 #Mean que esta en espera de aprobacion las fotos
                proyecto.save(update_fields=['aprobacion_fotos'])
            else:
                ctx = {'er': 'Recuerde que solo puede adjuntar archivos comprimidos Zip o Rar, el archivo debe contener las fotos de la Etapa actual de construccion para ser Revisadas por la Oficina Nacional', 'proyecto':proyecto}
                return render(request, 'main/error.html', ctx)            
        elif proyecto.etapa_actual == Etapa.CONS_P3:
            if request.FILES['fotos_p3'].name.split('.')[-1] == "zip" or request.FILES['fotos_p3'].name.split('.')[-1] == "rar":   
                form = FotosPCForm(request.POST, request.FILES, instance=adjuntos)
                form.save() 
                proyecto.aprobacion_fotos = 1 #Mean que esta en espera de aprobacion las fotos
                proyecto.save(update_fields=['aprobacion_fotos'])
            else:
                ctx = {'er': 'Recuerde que solo puede adjuntar archivos comprimidos Zip o Rar, el archivo debe contener las fotos de la Etapa actual de construccion para ser Revisadas por la Oficina Nacional', 'proyecto':proyecto}
                return render(request, 'main/error.html', ctx)             
        elif proyecto.etapa_actual == Etapa.DEDICACION:
            if request.FILES['dedicacion'].name.split('.')[-1] == "zip" or request.FILES['dedicacion'].name.split('.')[-1] == "rar":   
                form = DedicacionForm(request.POST, request.FILES, instance=adjuntos)
                form.save()
                proyecto.aprobacion_fotos = 1 #Mean que esta en espera de aprobacion las fotos
                proyecto.save(update_fields=['aprobacion_fotos'])
            else:
                ctx = {'er': 'Recuerde que solo puede adjuntar archivos comprimidos Zip o Rar, el archivo debe contener las fotos de la Etapa actual de construccion para ser Revisadas por la Oficina Nacional', 'proyecto':proyecto}
                return render(request, 'main/error.html', ctx) 
        mail_change_foto(proyecto, request.user) ##Envio email con notificando que se adjuntaron fotos   
        return redirect(proyecto)         
    raise Http404  


def hacer_login(request):

    NEXT = request.GET.get('next', "")

    if request.method == 'POST':
        
        form = LoginForm(data=request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user     = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                
                if request.POST.get('next', ""):
                    return redirect(request.POST['next'])

                return redirect('home')

        return render(request, 'main/login.html', {'loginForm': form, 'NEXT':NEXT})


    ctx = {'loginForm': LoginForm(), 'NEXT':NEXT}
    return render(request, 'main/login.html', ctx)


@login_required
def done(request, pk):

    proyecto  =  get_object_or_404(Edificacion, pk=pk)

    # validamos que el usuario tenga permiso de ver el proyecto
    if request.user.tipo != Usuario.LOCAL or request.user.pk != proyecto.usuario.pk:    #restriccion vertical y horizontal
        raise PermissionDenied
  
  
    ctx = {'proyecto': proyecto}
    return render(request, 'main/done.html', ctx)


def hacer_logout(request):
    logout(request)
    return redirect('hacer_login')



def evento(request,pk):
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/google-apps/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.
    FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                             request.user)
    FLOW.params['pk'] = pk
    authorize_url = FLOW.step1_get_authorize_url()
    return HttpResponseRedirect(authorize_url)   
   
def auth_return(request): 

      pk = FLOW.params['pk']      
      proyecto  =  get_object_or_404(Edificacion, pk=pk)
      etapa_inical_cons =  Etapa.objects.get(edificacion=proyecto,etapa=Etapa.CONS_P1)
 
      construction_initial = etapa_inical_cons.created
      construction_final = construction_initial

      credential = FLOW.step2_exchange(request.REQUEST) 
      http = httplib2.Http()
      http = credential.authorize(http)
      service = build("calendar", "v3", http=http)    

      for key,value in Etapa.ETAPA_ACTUAL:
        if key > Etapa.ESPERANDO_RECURSOS and key <= Etapa.DEDICACION:
            if proyecto.tipo_construccion >= 2 and key == Etapa.CONS_P1:
                construction_final = construction_final+timedelta(days=60)
            else:
                construction_final = construction_final+timedelta(days=40)   

            event = {
              'summary': proyecto.nombre_proyecto+' '+value,
              'location': proyecto.direccion,
              'description': 'Proyecto {} creado en {}, Fecha de {}'.format(proyecto.nombre_proyecto, proyecto.created, value),
              'start': {
                'date': construction_initial.strftime('%Y-%m-%d'),
                'timeZone': settings.TIME_ZONE,
              },              
              'end': {
                'date': construction_final.strftime('%Y-%m-%d'),
                'timeZone': settings.TIME_ZONE,
              },                    
              'reminders': {
                'useDefault': False,
                'overrides': [
                  {'method': 'email', 'minutes': 24 * 60},                 
                ],
              },
            }
            construction_initial = construction_final  
            event = service.events().insert(calendarId='primary', body=event).execute()
            print 'Event created: %s' % (event.get('htmlLink'))         

      ctx = {'hola':'chao'}
      return render(request, 'main/calendar.html', ctx)



def alert(request):

    edificaciones =  Edificacion.objects.filter(etapa_actual__gt=Etapa.ESPERANDO_RECURSOS,etapa_actual__lte=Etapa.DEDICACION)        
    var = []
    for proyecto in edificaciones:
        etapa_actual =  Etapa.objects.get(edificacion=proyecto,etapa=proyecto.etapa_actual)
        creacion_etapa_actual = etapa_actual.created
        percent = etapa_actual.percent                 
        if percent >= 90:#Si percent >= 90 notifico 
            if proyecto.aprobacion_fotos == 0: #0 -> Significa que no a subido fotos
                mail_recordatorio(proyecto)
                var.append({'proyecto':proyecto.nombre_proyecto , 'percent':percent , 'text':'Notificado'})         
            else:
                var.append({'proyecto':proyecto.nombre_proyecto , 'percent':percent , 'text':'Fotos Adjuntadas'})         
        else:
            var.append({'proyecto':proyecto.nombre_proyecto , 'percent':percent , 'text':'Aun No Cumple el Plazo'})   

    ctx = {'report':var}
    return render(request, 'main/cron_summary.html', ctx)

'''
    INFORMES SEMESTRALES DESDE FORMULARIO PUBLICO
'''
def informe_semestral_publico(request):

    form = InformeSemestralPublicoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        informe = form.save(commit=False)  
        informe.save()
        return redirect('informe_respuesta')

    return render(request, 'main/informe-semestral-publico.html', {'form': form})


def informe_semestral_edit(request, pk):

    if request.user.tipo not in [Usuario.NACIONAL, Usuario.SUPERADMIN]: 
        raise PermissionDenied

    informe  =  get_object_or_404(InformeSemestralPublico, pk=pk)

    form = InformeSemestralPublicoForm(request.POST or None, request.FILES or None, instance=informe)

    if form.is_valid():
        informe = form.save(commit=False)  
        informe.save()
        return redirect(informe_semestral)

    return render(request, 'main/informe-semestral-publico.html', {'form': form})


def informe_respuesta(request):
    return render(request, 'main/informe-semestral-publico-respuesta.html')


@login_required
def informes_semestrales(request):

    if request.user.tipo not in [Usuario.NACIONAL, Usuario.SUPERADMIN]: 
        raise PermissionDenied

    informes = InformeSemestralPublico.objects.all()

    return render(request, 'main/informes-semestrales.html', {'informes': informes})

@login_required
def informe_semestral(request, pk):

    if request.user.tipo not in [Usuario.NACIONAL, Usuario.SUPERADMIN]: 
        raise PermissionDenied

    informe  =  get_object_or_404(InformeSemestralPublico, pk=pk)
    
    return render(request, 'main/informe-semestral.html', {'informe':informe})


@login_required
def informe_semestral_csv(request, pk):

    if request.user.tipo not in [Usuario.NACIONAL, Usuario.SUPERADMIN]: 
        raise PermissionDenied
    
    inf  =  get_object_or_404(InformeSemestralPublico, pk=pk)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="%s.csv"' %inf.nombre_proyecto

    writer = csv.writer(response)
    row1 = []
    writer.writerow([
        'Nombre del Proyecto', 'Persona Encargada', 'Email', 'Teléfono',  
        'Región', 'Departamento', 'Municipio', 'Dirección',
        'Miembros', 'Nuevos miembros', 'Conversiones', 'Bautismos', 'Si no Bautismos',
        'Asistencia general', 'Grupos vida', 'Asistencia G.V.',
        'Plantación nombre 1', 'Plantación lugar 1', 'Plantación fecha 1',
        'Plantación nombre 2', 'Plantación lugar 2', 'Plantación fecha 2',
        'Plantación nombre 3', 'Plantación lugar 3', 'Plantación fecha 3',
        'Ofrendas', 'Peticiones', 'Testimonios', 'Actividades niños', 'Uso del local'])
    writer.writerow([
        inf.nombre_proyecto, inf.persona, inf.email, inf.telefono, 
        inf.get_region_display(), inf.depto, inf.municipio, inf.direccion,
        inf.miembros_actuales, inf.nuevos_miembros, inf.conversiones, inf.bautismos_nuevos, inf.no_bautismos,
        inf.asistencia_general, inf.grupos_vida, inf.asistencia_grupos,
        inf.plantacion_nombre_1, inf.plantacion_lugar_1, inf.plantacion_fecha_1,
        inf.plantacion_nombre_2, inf.plantacion_lugar_2, inf.plantacion_fecha_2,
        inf.plantacion_nombre_3, inf.plantacion_lugar_3, inf.plantacion_fecha_3,
        inf.ofrendas, inf.peticiones_oracion, inf.testimonios, inf.ministerio_ninos, inf.uso_local])

    return response




def mapa(request, filtro=None):
    
    proyectos = None
    ctx = {}

    todos = [2,3,4,5,6,7,8,9,10,11,12,13,14,15] # todos menos los que estan en diligenciamiento
    preaprobados = [2,3,4,5,6,7,8,9,10]
    contruccion = [11,12,13]
    dedicados = [14,15]


    if filtro:
        if filtro == 'preaprobados':
            proyectos = Edificacion.objects.filter(etapa_actual__in=preaprobados)
        if filtro == 'construccion':
            proyectos = Edificacion.objects.filter(etapa_actual__in=contruccion)
        if filtro == 'dedicados':
            proyectos = Edificacion.objects.filter(etapa_actual__in=dedicados)
    else:
        proyectos = Edificacion.objects.filter(etapa_actual__in=todos)

    ctx['proyectos'] = proyectos
        
    return render(request, 'main/mapa.html', ctx)

