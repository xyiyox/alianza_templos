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


@login_required
def proyecto(request, pk):
    # validamos que el proyecto exista
    #[EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, AdjuntosForm, CondicionesForm]
    proyecto  =  get_object_or_404(Edificacion, pk=pk)
   
    # validamos que el usuario tenga permiso de ver el proyecto
    if request.user.tipo == Usuario.LOCAL and request.user.pk != proyecto.usuario.pk:
        raise Http404 
   
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
        ctx['aprobacionArquitectoForm'] = AprobacionArquitectoForm(instance=proyecto)
        adj = proyecto.adjuntos_set.get()
        ctx['planosArquitectoForm'] = PlanosArquitectoForm(instance=adj)

    if request.user.tipo == Usuario.INGENIERO:
        ctx['aprobacionIngenieroForm'] = AprobacionIngenieroForm(instance=proyecto) 

    if request.user.tipo == Usuario.TESORERO:
        ctx['aprobacionTesoreroForm'] = AprobacionTesoreroForm(instance=proyecto) 
    
    if request.user.tipo == Usuario.NACIONAL:
        ctx['aprobacionNacionalForm'] = AprobacionNacionalForm(instance=proyecto) 
        asignarUsuariosForm = AsignarUsuariosForm(instance=proyecto)
        asignarUsuariosForm.helper.form_action = reverse('asignaciones', args=[proyecto.pk])
        ctx['asignarUsuariosForm'] = asignarUsuariosForm
        #Por si el Nacional lo aprueba sin requerir el arquitecto
        ctx['aprobacionArquitectoForm'] = AprobacionArquitectoForm(instance=proyecto)
    
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

            #form = AprobacionNacionalForm(request.POST, instance=proyecto)
            #print (request.POST.get('aprobacion_nacional', False))   
            # if 'fromN' in request.POST:               
            #     if not proyecto.aprobacion_tesorero:                    
            #         ctx={'proyecto':proyecto,'er':'el tesorero debe autorizar el proyecto'}                                         
            #         return render(request, 'main/error.html',ctx)                   
            #     else:
            #         proyecto.aprobacion_nacional = request.POST.get('aprobacion_nacional', False)           
            #         if proyecto.aprobacion_nacional:
            #             registrar_etapa(proyecto, Etapa.APROB_INTERNACIONAL)  
            #             mail_change_etapa(proyecto, request.user) 
            #             proyecto.save(update_fields=['aprobacion_nacional'])
            #         else:   
            #             if proyecto.etapa_actual == 8:  
            #                 registrar_etapa(proyecto, Etapa.APROB_NACIONAL)  
            #                 mail_change_etapa(proyecto, request.user) 
            #                 proyecto.save(update_fields=['aprobacion_nacional'])                  
            #             else:
            #                 ctx={'proyecto':proyecto,'er':'No puede Desautorizar el proyecto despues de avanzar en etapas'}                                         
            #                 return render(request, 'main/error.html',ctx)     
            # else:                
            #     proyecto.aprobacion_arquitecto = request.POST.get('aprobacion_arquitecto', False)           
            #     if proyecto.aprobacion_arquitecto :
            #         var=False 
            #     else:
            #         var=True
            #     proyecto.requiere_arquitecto   = var   
            #     proyecto.save(update_fields=['aprobacion_arquitecto','requiere_arquitecto'])



         
        if request.user.tipo == Usuario.ARQUITECTO:
            #form = AprobacionArquitectoForm(request.POST, request.FILES, instance=proyecto)
          
            proyecto.aprobacion_arquitecto = request.POST.get('aprobacion_arquitecto', False)           
            if proyecto.aprobacion_arquitecto:   
                if proyecto.etapa_actual == 4:                
                    adj = proyecto.adjuntos_set.get()
                    form_plano = PlanosArquitectoForm(request.POST, request.FILES, instance=adj)
                    if form.is_valid() and form_plano.is_valid():
                        print('Somos Validos')
                        form.save()
                        form_plano.save()    
                        proyecto.save(update_fields=['aprobacion_arquitecto'])    
                        registrar_etapa(proyecto, Etapa.APROB_INGENIERO)  
                        mail_change_etapa(proyecto, request.user)                     
                    else:
                        print('No Somos Validos', form.errors, form_plano.errors)               
            else:
                if proyecto.etapa_actual == 5: 
                    registrar_etapa(proyecto, Etapa.PLANOS)  
                    mail_change_etapa(proyecto, request.user) 
                    proyecto.save(update_fields=['aprobacion_arquitecto'])          
                else:
                    ctx={'proyecto':proyecto,'er':'No puede Desautorizar el proyecto despues de avanzar en etapas'}                                         
                    return render(request, 'main/error.html',ctx)         
        if request.user.tipo == Usuario.INGENIERO:
            #form = AprobacionIngenieroForm(request.POST, instance=proyecto)            
            if not proyecto.aprobacion_arquitecto:                               
                ctx={'proyecto':proyecto,'er':'el arquitecto debe autorizar el proyecto'}                                         
                return render(request, 'main/error.html',ctx) 
            else:                
                proyecto.aprobacion_ingeniero = request.POST.get('aprobacion_ingeniero', False)           
                if proyecto.aprobacion_ingeniero:
                    if proyecto.etapa_actual == 5:
                        registrar_etapa(proyecto, Etapa.APROB_TESORERO)  
                        mail_change_etapa(proyecto, request.user) 
                        proyecto.save(update_fields=['aprobacion_ingeniero']) 
                else: 
                    if proyecto.etapa_actual == 6:
                        registrar_etapa(proyecto, Etapa.APROB_INGENIERO)  
                        mail_change_etapa(proyecto, request.user) 
                        proyecto.save(update_fields=['aprobacion_ingeniero']) 
                    else:
                        ctx={'proyecto':proyecto,'er':'No puede Desautorizar el proyecto despues de avanzar en etapas'}                                         
                        return render(request, 'main/error.html',ctx)                 

        if request.user.tipo == Usuario.TESORERO:   
            #form = AprobacionTesoreroForm(request.POST, instance=proyecto)
            #el maestro de obra no la a aprobado
            if not proyecto.aprobacion_ingeniero:               
                ctx={'proyecto':proyecto,'er':'el director de obra debe autorizar el proyecto'}                                         
                return render(request, 'main/error.html',ctx)                   
            else:
                proyecto.aprobacion_tesorero = request.POST.get('aprobacion_tesorero', False)           
                if proyecto.aprobacion_tesorero:
                    if proyecto.etapa_actual == 6:
                        registrar_etapa(proyecto, Etapa.APROB_NACIONAL)  
                        mail_change_etapa(proyecto, request.user) 
                        proyecto.save(update_fields=['aprobacion_tesorero']) 
                else:
                    if proyecto.etapa_actual == 7:
                        registrar_etapa(proyecto, Etapa.APROB_TESORERO)  
                        mail_change_etapa(proyecto, request.user)                    
                        proyecto.save(update_fields=['aprobacion_tesorero'])    
                    else:
                        ctx={'proyecto':proyecto,'er':'No puede Desautorizar el proyecto despues de avanzar en etapas'}                                         
                        return render(request, 'main/error.html',ctx)     
        

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

        form = AsignarUsuariosForm(request.POST, instance=proyecto)
        form.save()
 
        return redirect(proyecto)

    raise Http404


class Aplicacion(SessionWizardView):

    template_name = "main/aplicacion.html"
    
    form_list = [EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, AdjuntosForm, CondicionesForm]

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tmp'))
   
    def done(self, form_list, form_dict, **kwargs):
        edificacion = form_dict['0'].instance
        print('Paso nro 1...', edificacion)
        return redirect('done', pk=edificacion.id )

    def get(self, request, *args, **kwargs):
        """
        This method handles GET requests.

        If a GET request reaches this point, the wizard assumes that the user
        just starts at the first step or wants to restart the process.
        The data of the wizard will be resetted before rendering the first step.
        """
        #Solo el local tiene acceso al form wizzard ningun otro
        if request.user.tipo != Usuario.LOCAL:
            raise Http404 


        self.storage.reset()

        # reset the current step to the first step.
        self.storage.current_step = self.steps.first
        
        # Se mira cuantos proyectos tiene creados el usuario actual
        cant_proyectos = Edificacion.objects.filter(usuario=request.user).count()
        # Se obtiene la pk para saber si se va a editar un proyecto o no
        pk = self.kwargs.get('pk', None)
        
        # Si el usuario ya tiene 2 proyectos creados se lo redirige al home
        if cant_proyectos == 2 and not pk:
            return redirect('home')
        else:
            if 'redireccion' in self.kwargs:
                self.storage.current_step = '1'
            return self.render(self.get_form())

    def render_done(self, form, **kwargs):
        """
        This method gets called when all forms passed. The method should also
        re-validate all steps to prevent manipulation. If any form fails to
        validate, `render_revalidation_failure` should get called.
        If everything is fine call `done`.
        """
        final_forms = OrderedDict()
        # walk through the form list and try to validate the data again.
        for form_key in self.get_form_list():
            form_obj = self.get_form(step=form_key,
                data=self.storage.get_step_data(form_key),
                files=self.storage.get_step_files(form_key))
            # Quitamos la re validacion de los form debido a que no es necesaria
            # y da conflictos para redirigir al metodo done
            # if not form_obj.is_valid():
            #     return self.render_revalidation_failure(form_key, form_obj, **kwargs)
            final_forms[form_key] = form_obj

        # render the done view and reset the wizard before returning the
        # response. This is needed to prevent from rendering done with the
        # same data twice.
        done_response = self.done(final_forms.values(), form_dict=final_forms, **kwargs)
        self.storage.reset()
        return done_response

    def get_form_instance(self, step):
        
        # Recibo el pk argument que llega por el request url
        pk = self.kwargs.get('pk', None)
        
        # cargamos las instancias solo si estamos en modo edicion
        if pk:
            # pedimos el primer modelo
            model_0 = Edificacion.objects.get(pk=pk)   
            # Resetea el diccionario de instancias
            self.instance_dict.clear()
            self.instance_dict['0'] = model_0
            
            try:
                # pedimos el segundo modelo
                model_1 = InformacionFinanciera.objects.get(edificacion=pk)
                self.instance_dict['1'] = model_1
            except InformacionFinanciera.DoesNotExist:
                print("No existe InformacionFinanciera")
            
            try:
                # pedimos el segundo modelo
                model_2 = Comunidad.objects.get(edificacion=pk)
                self.instance_dict['2'] = model_2
            except Comunidad.DoesNotExist:
                print("No existe Comunidad")

            try:
                # pedimos el segundo modelo
                model_3 = Congregacion.objects.get(edificacion=pk)
                self.instance_dict['3'] = model_3
            except Congregacion.DoesNotExist:
                print("No existe Congregacion")

            try:
                # pedimos el segundo modelo
                model_4 = Adjuntos.objects.get(edificacion=pk)
                self.instance_dict['4'] = model_4
            except Adjuntos.DoesNotExist:
                print("No existe Adjuntos")

            try:
                # pedimos el segundo modelo
                model_5 = Condiciones.objects.get(edificacion=pk)
                self.instance_dict['5'] = model_5
            except Condiciones.DoesNotExist:
                print("No existe Condiciones")
        return self.instance_dict.get(step, None)
        
    
    def get_context_data(self, form, **kwargs):

        context = super(Aplicacion, self).get_context_data(form=form, **kwargs)
       
        context.update({'form_list': self.form_list})

        model_1 = self.instance_dict.get('0', False) 
        if model_1:
            # paso el valor del campo estado en el form 1
            context.update({"proyecto": model_1, 'estado': model_1.estado})
        else:
            # si no existe le envio -1 
            context.update({'estado': -1})

        #if self.steps.current == '1':
        #    context.update({'fuentes': FuentesFinanciacionForm()})
        return context

    def render_next_step(self, form, **kwargs):
        """ Redireccionamos el form para usarlo en modo edit"""
        
        if not self.kwargs.get('pk', None):  # verificamos que estemos en modo creacion

            if self.steps.current == '0':    # actuamos solo si es el paso 1
                model_1 = self.instance_dict.get('0', False) # obtenemos el pk del modelo que acabamos de crear
                self.storage.reset()
                # redirecionamos al mismo objeto pero en edicion, trabaja con ayuda de get()
                return redirect(reverse('proyecto_edit_redirect', kwargs={'pk': model_1.pk, 'redireccion':1} ))  
        
        # en los otros paso, que la aplicacion funcione por defecto
        return super(Aplicacion, self).render_next_step(form, **kwargs)

    
    def process_step(self, form):
        """ 
        Metodo que procesa cada formulario al momento de ser enviado (submit)
        """
        step_current = self.steps.current


        if step_current == '0':
            
            if self.instance_dict.get('0', False):
                # Esto sucede cuando se esta editanto el primer formulario
                form.save()
            else: 
                model_instance              = form.save(commit=False)
                model_instance.estado       = step_current
                model_instance.usuario      = self.request.user
                model_instance.etapa_actual = Etapa.DILIGENCIAMIENTO   
                model_instance.save()
                self.instance_dict['0'] = model_instance
                # Registramos la etapa de Diligenciamiento
                registrar_etapa(model_instance, Etapa.DILIGENCIAMIENTO)

        else:
            if self.instance_dict.get(step_current, False): 
                form.save()
            else:
                # Se almacena con commit False el formulario actual
                instance    = form.save(commit=False)    
                edificacion = self.instance_dict['0']   
                # Se almacena la instancia del formulario actual con el id de la edificacion
                instance.edificacion = edificacion
                instance.save()
                self.instance_dict[step_current] = instance
                # Fijar el estado del formulario en el modelo edificacion
                edificacion.estado = step_current
                edificacion.save(update_fields=['estado'])

                # Notificar el cambio de etapa al enviar el ultimo formulario
                if step_current == self.steps.last:
                    registrar_etapa(edificacion, Etapa.APROB_REGIONAL)
                    #etapa = Etapa(edificacion=edificacion, etapa=Etapa.APROB_REGIONAL)
                    #etapa.save()
                    # send email notification
                    mail_change_etapa(edificacion, self.request.user)

        return self.get_form_step_data(form)
    
    def render_goto_step(self, goto_step, **kwargs):
        """
        This method gets called when the current step has to be changed.
        `goto_step` contains the requested step to go to.
        """
        # Resetear el storage garantiza que se puedan observar 
        # los cambios hechos en los archivos adjuntos
        self.storage.reset()
        print('render_goto_step y resetie el storage')
        self.storage.current_step = goto_step        
        form = self.get_form(
            data=self.storage.get_step_data(self.steps.current),
            files=self.storage.get_step_files(self.steps.current))
        print('form data=', form.data)
        print('form files=', form.files)
        return self.render(form)

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
    if request.user.tipo == Usuario.LOCAL and request.user.pk != proyecto.usuario.pk:
        raise Http404 
    
    ctx = {'proyecto': proyecto}
    print('Paso nro 2...')
    return render(request, 'main/done.html', ctx)


def hacer_logout(request):
    logout(request)
    return redirect('hacer_login')