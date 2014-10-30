# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import WizardView, SessionWizardView
from django.core.files.storage import FileSystemStorage

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

    if request.user.tipo != Usuario.NACIONAL:   # validamos que el usuario tenga permiso de ver esta vista
        raise PermissionDenied 
        
    proyectos = Edificacion.objects.all()
    ctx = {'proyectos': proyectos}
    return render(request, 'main/home-nacional.html', ctx)


@login_required
def home_regional(request):

    if request.user.tipo != Usuario.REGIONAL:   # validamos que el usuario tenga permiso de ver esta vista
        raise PermissionDenied 

    users_hijos = Usuario.objects.filter(user_padre__exact=request.user.pk).values('pk')  # Obtengo los usuarios que son hijos del regional
    proyectos = Edificacion.objects.filter(usuario__in=users_hijos)

    ctx = {'proyectos': proyectos}
    return render(request, 'main/home-regional.html', ctx)


@login_required
def home_local(request):

    if request.user.tipo != Usuario.LOCAL:   # validamos que el usuario tenga permiso de ver esta vista
        raise PermissionDenied 

    proyectos = Edificacion.objects.filter(usuario__exact=request.user.pk)
    ctx = {'proyectos': proyectos}
    return render(request, 'main/home-local.html', ctx)


@login_required
def ver_comentarios(request, pk):
    form = ComentarioForm()
    comentarios = Comentario.objects.filter(edificacion=pk)
    ctx = {'comentarios': comentarios, 'form': form}
    return render(request, 'main/comentarios.html', ctx)


@login_required
def proyecto(request, pk):
    
    proyecto  =  get_object_or_404(Edificacion, pk=pk)  # validamos que el proyecto exista

    if request.user.tipo == Usuario.LOCAL and request.user.pk != proyecto.usuario.pk:   # validamos que el usuario tenga permiso de ver el proyecto
        raise Http404 
   
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            new_coment = form.save(commit=False)
            new_coment.edificacion = proyecto
            new_coment.commenter = request.user
            new_coment.save()
            return redirect(proyecto) # redirect funciona con el objeto si en el existe el metodo get_absolute_url

    
    comentarios  = Comentario.objects.filter(edificacion=pk).order_by('-created')
    form         = ComentarioForm()
    form.helper.form_action = proyecto.get_absolute_url()

    ctx = {'proyecto': proyecto, 'comentarios': comentarios, 'form': form}
    
    return render(request, 'main/proyecto.html', ctx)




class Aplicacion(SessionWizardView):

    template_name = "main/aplicacion.html"

    form_list = [EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, AdjuntosForm, CondicionesForm]

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'tmp'))

    def get_form_initial(self, step):
        # Fijar el valor solicitado dependiendo del tipo de construccion elegido en el formulario edificacion
        if step == '1':
            edificacion = self.instance_dict['0']
            return self.initial_dict.get(step, {'valor_solicitado': edificacion.tipo_construccion})

        return self.initial_dict.get(step, {})

    
    def done(self, form_list, **kwargs):
        # AQUI VA LA LOGICA PARA PROCESAR TODO EL WIZAR AL FINAL DE TODOS LOS PASOS
        return render_to_response('main/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


    def get_form_instance(self, step):
        
        pk = self.kwargs.get('pk', None)  # Recibo el pk argument que llega por el reques url
        
        # cargamos las instancias solo si estamos en modo edicion
        if pk:   
            model_0 = Edificacion.objects.get(pk=pk)   # pedimos el primer modelo
            self.instance_dict['0'] = model_0
            
            try:
                model_1 = InformacionFinanciera.objects.get(edificacion=pk)  # pedimos el segundo modelo
                self.instance_dict['1'] = model_1
            except InformacionFinanciera.DoesNotExist:
                print "No existe InformacionFinanciera"
            
            try:
                model_2 = Comunidad.objects.get(edificacion=pk)  # pedimos el segundo modelo
                self.instance_dict['2'] = model_2
            except Comunidad.DoesNotExist:
                print "No existe Comunidad"

            try:
                model_3 = Congregacion.objects.get(edificacion=pk)  # pedimos el segundo modelo
                self.instance_dict['3'] = model_3
            except Congregacion.DoesNotExist:
                print "No existe Congregacion"

            try:
                model_4 = Adjuntos.objects.get(edificacion=pk)  # pedimos el segundo modelo
                self.instance_dict['4'] = model_4
            except Adjuntos.DoesNotExist:
                print "No existe Adjuntos"

            try:
                model_5 = Condiciones.objects.get(edificacion=pk)  # pedimos el segundo modelo
                self.instance_dict['5'] = model_5
            except Condiciones.DoesNotExist:
                print "No existe Condiciones"

        return self.instance_dict.get(step, None)
        
    
    def get_context_data(self, form, **kwargs):
        context = super(Aplicacion, self).get_context_data(form=form, **kwargs)

       
        context.update({'form_list': self.form_list})
        
        model_1 = self.instance_dict.get('0', False) 
        if model_1:
            context.update({'estado': model_1.estado}) # paso el valor del campo estado en el form 1
        else:
            context.update({'estado': -1}) # si no existe le envio -1 

        if self.steps.current == '1':
            context.update({'fuentes': FuentesFinanciacionForm()})
        return context

    
    def process_step(self, form):
        """ Metodo que procesa cada formulario al momento de ser enviado (submit) """

        step_current = form.data['aplicacion-current_step']


        # Para el primer formulario se captura el id (pk) de la edificacion para usarlo en los otros formularios
        if step_current == '0':
            
            if self.instance_dict.get('0', False): #.get('edificacion_pk','') != '':
                form.save() # Esto sucede cuando se esta editanto el primer formulario
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
                instance    = form.save(commit=False)       # Se almacena con commit False el formulario actual
                edificacion = self.instance_dict['0']   # Edificacion.objects.get(pk=data1['edificacion_pk'])
                # Se almacena la instancia del formulario actual con el id de la edificacion
                instance.edificacion = edificacion
                instance.save()
                self.instance_dict[step_current] = instance

                edificacion.estado = step_current   # Fijar el estado del formulario en el modelo edificacion
                # Indicar que esta en etapa de Diligenciamiento
                edificacion.etapa_actual = Edificacion.ETAPA_ACTUAL[0][0]
                edificacion.save()

        return self.get_form_step_data(form)


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

def hacer_logout(request):
    logout(request)
    return redirect('hacer_login') 