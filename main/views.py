# -*- coding: utf-8 -*-
import os

from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect  
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core.urlresolvers import reverse
from threading import Timer

from main.forms import *
from main.email import *
from db.forms import *
from db.models import Edificacion, Comunidad, Comentario, Etapa
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
def home_otros(request):
    # validamos que el usuario tenga permiso de ver esta vista
    users = [Usuario.LOCAL, Usuario.REGIONAL, Usuario.NACIONAL]
    if request.user.tipo in users:
        raise PermissionDenied 
    if request.user.tipo == Usuario.ARQUITECTO: 
        proyectos = Edificacion.objects.filter(arquitecto__exact=request.user.pk)
    if request.user.tipo == Usuario.INGENIERO:
        proyectos = Edificacion.objects.filter(ingeniero__exact=request.user.pk)
    if request.user.tipo == Usuario.TESORERO:
        proyectos = Edificacion.objects.filter(tesorero__exact=request.user.pk)

    ctx = {'proyectos': proyectos}
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

    # OJO VALIDAR QUE EN CREACION NO SE PUEDA SALTAR EL ORDEN ESTRICTO DE FORMULARIOS

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
    #print form.instance
    
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
                    #mail_change_etapa(proyecto, self.request.user)

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
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.foto_construccion.url]
    if adjuntos.foto_congregacion:
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.foto_congregacion.url]
    if adjuntos.foto_pastor:
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.foto_pastor.url]
    if adjuntos.permiso_construccion: 
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.permiso_construccion.url]
    if adjuntos.escritura_terreno:   
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.escritura_terreno.url]
    if adjuntos.manzana_catastral:    
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.manzana_catastral.url]
    if adjuntos.plan_construccion:    
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.plan_construccion.url]    
    if adjuntos.historia_congregacion:    
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.historia_congregacion.url]    
    if adjuntos.testimonio_pastor:    
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.testimonio_pastor.url]    
    if adjuntos.planos_arquitecto:    
        filenames += [os.path.dirname(os.path.abspath(__file__))+"/../public"+adjuntos.planos_arquitecto.url]                

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
def proyecto(request, pk):
    # validamos que el proyecto exista
    #[EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, AdjuntosForm, CondicionesForm]
    proyecto  =  get_object_or_404(Edificacion, pk=pk)
   
    # validamos que el usuario tenga permiso de ver el proyecto
    if request.user.tipo == Usuario.LOCAL and request.user.pk != proyecto.usuario.pk:
        raise PermissionDenied 
   
    if request.method == 'POST':        
        form = ComentarioForm(request.POST)
        if form.is_valid():
            new_coment = form.save(commit=False)
            new_coment.edificacion = proyecto
            new_coment.commenter = request.user
            new_coment.save()

            result_email = mail_comentario(new_coment, proyecto)
            # redirect funciona con el objeto si en el existe el metodo get_absolute_url
            return redirect(proyecto)

    comentarios  = Comentario.objects.filter(edificacion=pk).order_by('-created')
    comentarioForm         = ComentarioForm()
    comentarioForm.helper.form_action = proyecto.get_absolute_url()

    ctx = {'proyecto': proyecto, 'Etapa': Etapa, 'comentarios': comentarios, 'comentarioForm': comentarioForm}
    ctx['aprobacionForm'] = AprobacionForm()  
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
            
            if proyecto.etapa_actual == Etapa.ASIGN_USUARIOS and 'aprobar' in request.POST:
                proyecto.usuarios_asignados = request.POST['aprobar']
                proyecto.save(update_fields=['usuarios_asignados'])

                registrar_etapa(proyecto, Etapa.PLANOS)
                mail_change_etapa(proyecto, request.user)

            if proyecto.etapa_actual == Etapa.APROB_NACIONAL and 'aprobar' in request.POST:
                proyecto.aprobacion_nacional = request.POST['aprobar']
                proyecto.save(update_fields=['aprobacion_nacional'])

                registrar_etapa(proyecto, Etapa.APROB_INTERNACIONAL)
                mail_change_etapa(proyecto, request.user)

            if proyecto.etapa_actual == Etapa.APROB_INTERNACIONAL and 'aprobar' in request.POST:
                proyecto.aprobacion_internacional = request.POST['aprobar']
                proyecto.save(update_fields=['aprobacion_internacional'])

                registrar_etapa(proyecto, Etapa.ESPERANDO_RECURSOS)
                mail_change_etapa(proyecto, request.user)    

            if proyecto.etapa_actual == Etapa.ESPERANDO_RECURSOS and 'aprobar' in request.POST:       

                proyecto.envio_icm = request.POST['aprobar']
                proyecto.save(update_fields=['envio_icm'])

                proyecto.envio_alianza = request.POST['aprobar']
                proyecto.save(update_fields=['envio_alianza'])         

                registrar_etapa(proyecto, Etapa.CONS_P1)
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