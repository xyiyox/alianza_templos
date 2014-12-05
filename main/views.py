# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView, NamedUrlSessionWizardView
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse

from main.forms import *
from db.forms import *

from django.conf import settings
import os
from db.models import Edificacion, Comentario
from usuarios.models import Usuario


def home(request):

    if request.user.is_authenticated():
        
        if request.user.tipo == Usuario.NACIONAL:
            return redirect('home_nacional')

        if request.user.tipo == Usuario.REGIONAL:
            return redirect('home_regional')

        if request.user.tipo == Usuario.LOCAL:
            return redirect('home_local')

        
        
    return redirect('hacer_login')




@login_required
def home_nacional(request):
    # validamos que el usuario tenga permiso de ver esta vista
    if request.user.tipo != Usuario.NACIONAL:
        raise PermissionDenied 
        
    proyectos = Edificacion.objects.all()
    ctx = {'proyectos': proyectos}
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
            # redirect funciona con el objeto si en el existe el metodo get_absolute_url
            return redirect(proyecto)

    
    comentarios  = Comentario.objects.filter(edificacion=pk).order_by('-created')
    comentarioForm         = ComentarioForm()
    comentarioForm.helper.form_action = proyecto.get_absolute_url()

    ctx = {'proyecto': proyecto, 'comentarios': comentarios, 'comentarioForm': comentarioForm}
    ctx['aprobacionRegionalForm'] = AprobacionRegionalForm(instance=proyecto)
    
    return render(request, 'main/proyecto.html', ctx)

@login_required
def autorizaciones(request, pk):
    if request.method == 'POST':
        proyecto  =  get_object_or_404(Edificacion, pk=pk)
        form = AprobacionRegionalForm(request.POST, instance=proyecto)
        form.save()
        return redirect('proyecto', pk)
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
        step_current = form.data['aplicacion-current_step']

        # Para el primer formulario se captura el id (pk) de la edificacion para usarlo en los otros formularios
        if step_current == '0':
            
            if self.instance_dict.get('0', False):
                # Esto sucede cuando se esta editanto el primer formulario
                form.save()
            else: 
                model_instance              = form.save(commit=False)
                model_instance.estado       = step_current
                model_instance.usuario      = self.request.user
                # Indicar que esta en etapa de Diligenciamiento
                model_instance.etapa_actual = Edificacion.ETAPA_ACTUAL[0][0]
                model_instance.save()
                self.instance_dict['0'] = model_instance
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
                # Indicar que esta en etapa de Diligenciamiento
                edificacion.etapa_actual = Edificacion.ETAPA_ACTUAL[0][0]
                edificacion.save()
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