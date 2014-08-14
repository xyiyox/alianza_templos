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


def home(request):

	if request.user.is_authenticated():
		return render(request, 'main/home.html')

	return redirect('hacer_login')

class Aplicacion(SessionWizardView):

	template_name = "main/aplicacion.html"
	
	form_list = [EdificacionForm, InformacionFinancieraForm, ComunidadForm, CongregacionForm, FuentesFinancierasForm, CondicionesForm]

	def done(self, form_list, **kwargs):
		# AQUI VA LA LOGICA PARA PROCESAR TODO EL WIZAR AL FINAL DE TODOS LOS PASOS
		return render_to_response('main/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
        
	#file_storage = FileSystemStorage(location=MEDIA_URL+'fotos/')
	file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

	def process_step(self, form):
		#form.data['estado'] = form.data['aplicacion-current_step']
		#model = self.get_form_instance(form.data['aplicacion-current_step'])
		print form.data
		#print model
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