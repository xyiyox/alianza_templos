# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView

from main.forms import *
from db.forms import *




def home(request):

	if request.user.is_authenticated():
		return render(request, 'main/home.html')

	return redirect('hacer_login')


class Aplicacion(SessionWizardView):

	template_name = "main/aplicacion.html"
	
	form_list = [EdificacionForm, ComunidadForm]


	def get_form(self, step=None, data=None, files=None):
		form = super(Aplicacion, self).get_form(step, data, files)

		# determine the step if not given
		if step is None:
		    step = self.steps.current

		# AQUI VA LA LOGICA PARA PROCESAR CADA FORM INDEPENDIENTE EN CADA PASO    
		return form


	def done(self, form_list, **kwargs):
		# AQUI VA LA LOGICA PARA PROCESAR TODO EL WIZAR AL FINAL DE TODOS LOS PASOS
		return render_to_response('main/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
	


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