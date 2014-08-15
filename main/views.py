# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import WizardView, SessionWizardView

from django.core.files.storage import FileSystemStorage

from main.forms import *
from db.forms import *

from django.conf import settings
import os
from db.models import Edificacion


def home(request):

	if request.user.is_authenticated():
		return render(request, 'main/home.html')

	return redirect('hacer_login')

class Aplicacion(SessionWizardView):

	template_name = "main/aplicacion.html"
	
	initial = {
		'1': {'fuentes': FuentesFinanciacionForm()},
	}

	initial_dict = initial

	form_list = [EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, AdjuntosForm, CondicionesForm]


	def done(self, form_list, **kwargs):
		# AQUI VA LA LOGICA PARA PROCESAR TODO EL WIZAR AL FINAL DE TODOS LOS PASOS
		return render_to_response('main/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
        
	#file_storage = FileSystemStorage(location=MEDIA_URL+'fotos/')
	file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

	def process_step(self, form):
		""" Metodo que procesa cada formulario al momento de ser enviado (submit) """

		step_current = form.data['aplicacion-current_step']


		# Para el primer formulario se captura el id (pk) de la edificacion para usarlo en los otros formularios
		if step_current == '0':
			
			if self.instance_dict.get('0', False): #.get('edificacion_pk','') != '':
				form.save()
			else: 
				model_instance 				= form.save(commit=False)
				model_instance.estado 		= step_current
				model_instance.save()
				self.instance_dict['0'] = model_instance		
		else:
			if self.instance_dict.get(step_current, False): 
				form.save()
			else:
				instance 	= form.save(commit=False)		# Se almacena con commit False el formulario actual
				edificacion = self.instance_dict['0']	# Edificacion.objects.get(pk=data1['edificacion_pk'])
				# Se almacena la instancia del formulario actual con el id de la edificacion
				instance.edificacion = edificacion
				instance.save()
				self.instance_dict[step_current] = instance

				edificacion.estado = step_current	# Fijar el estado del formulario en el modelo edificacion
				edificacion.save()

		return self.get_form_step_data(form)


def hacer_login(request):

	if request.method == 'POST':
		print "ES POST"
		form = LoginForm(data=request.POST)
		print form
		if form.is_valid():
			print "ES VALID"
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None and user.is_active:
				login(request, user)
				return redirect('home')
		return render(request, 'main/login.html', {'loginForm': form})


	ctx = {'loginForm': LoginForm()}
	return render(request, 'main/login.html', ctx)

def hacer_logout(request):
    logout(request)
    return redirect('hacer_login') 