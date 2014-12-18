# -*- coding: utf-8 -*-
import os

from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
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
from db.models import Edificacion, Comentario, Etapa
from usuarios.models import Usuario


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
    ctx = {'Etapa':Etapa()}
    
    if etapa:
        proyectos = Edificacion.objects.filter(etapa_actual=etapa)  
        ctx['etapa_actual'] = int(etapa) 
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

    ctx = {'proyecto': proyecto, 'comentarios': comentarios, 'comentarioForm': comentarioForm}

    if request.user.tipo == Usuario.REGIONAL:
        ctx['aprobacionRegionalForm'] = AprobacionRegionalForm(instance=proyecto)  
        
    if request.user.tipo == Usuario.ARQUITECTO:
        ctx['aprobacionArquitectoForm'] = AprobacionArquitectoForm(instance=proyecto) 

    if request.user.tipo == Usuario.INGENIERO:
        ctx['aprobacionIngenieroForm'] = AprobacionIngenieroForm(instance=proyecto) 

    if request.user.tipo == Usuario.TESORERO:
        ctx['aprobacionTesoreroForm'] = AprobacionTesoreroForm(instance=proyecto) 
    
    if request.user.tipo == Usuario.NACIONAL:
        ctx['aprobacionNacionalForm'] = AprobacionNacionalForm(instance=proyecto) 
        asignarUsuariosForm = AsignarUsuariosForm(instance=proyecto)
        asignarUsuariosForm.helper.form_action = reverse('asignaciones', args=[proyecto.pk])
        ctx['asignarUsuariosForm'] = asignarUsuariosForm
    
    return render(request, 'main/proyecto.html', ctx)



def registrar_etapa(edificacion, etapa):
    _etapa = Etapa(edificacion=edificacion, etapa=etapa)
    _etapa.save()

@login_required
def autorizaciones(request, pk):

    if request.method == 'POST':
        proyecto  =  get_object_or_404(Edificacion, pk=pk)
       
        if request.user.tipo == Usuario.REGIONAL:
            
            proyecto.aprobacion_regional = request.POST.get('aprobacion_regional', False) 
            proyecto.etapa_actual = Etapa.ASIGN_USUARIOS
            proyecto.save(update_fields=['aprobacion_regional', 'etapa_actual'])
            
            registrar_etapa(proyecto, Etapa.ASIGN_USUARIOS)  
            mail_change_etapa(proyecto, request.user)
            
        
        if request.user.tipo == Usuario.ARQUITECTO:
            form = AprobacionArquitectoForm(request.POST, instance=proyecto)

        if request.user.tipo == Usuario.INGENIERO:
            form = AprobacionIngenieroForm(request.POST, instance=proyecto)

        if request.user.tipo == Usuario.TESORERO:
            form = AprobacionTesoreroForm(request.POST, instance=proyecto)

        if request.user.tipo == Usuario.NACIONAL:
            form = AprobacionNacionalForm(request.POST, instance=proyecto)

       

        return redirect(proyecto)

    raise Http404 


@login_required
def asignaciones(request, pk):
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
        return redirect('done', pk=edificacion.id )

    
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

        if self.steps.current == '1':
            context.update({'fuentes': FuentesFinanciacionForm()})
        return context

    
    def process_step(self, form):
        """ 
        Metodo que procesa cada formulario al momento de ser enviado (submit)
        """
        step_current = form.data['aplicacion-current_step']   # esto es innecesario ya que self.steps.current hace los mismo


        if step_current == '0':
            
            if self.instance_dict.get('0', False):
                # Esto sucede cuando se esta editanto el primer formulario
                form.save()
            else: 
                model_instance              = form.save(commit=False)
                model_instance.estado       = step_current
                model_instance.usuario      = self.request.user
                # Indicar que esta en etapa de Diligenciamiento
                model_instance.etapa_actual = Etapa.DILIGENCIAMIENTO
                model_instance.save()
                self.instance_dict['0'] = model_instance
                # registamos la etapa 
                etapa = Etapa(edificacion=model_instance, etapa=Etapa.DILIGENCIAMIENTO)
                etapa.save()
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

                # notificar el cambio de etapa al enviar el ultimo formulario
                if step_current == self.steps.last:
                    edificacion.etapa_actual = Etapa.APROB_REGIONAL
                    edificacion.save(update_fields=['etapa_actual'])
                    
                    etapa = Etapa(edificacion=edificacion, etapa=Etapa.APROB_REGIONAL)
                    etapa.save()
                    # send email notification
                    mail_change_etapa(edificacion, self.request.user)

        return self.get_form_step_data(form)
    
    def render_goto_step(self, goto_step, **kwargs):
        """
        This method gets called when the current step has to be changed.
        `goto_step` contains the requested step to go to.
        """
        self.storage.reset()
        self.storage.current_step = goto_step        
        form = self.get_form(
            data=self.storage.get_step_data(self.steps.current),
            files=self.storage.get_step_files(self.steps.current))
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
    return render(request, 'main/done.html', ctx)


def hacer_logout(request):
    logout(request)
    return redirect('hacer_login') 