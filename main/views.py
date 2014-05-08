# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from main.forms import *



def home(request):

	if request.user.is_authenticated():
		return render(request, 'main/home.html')

	return redirect('hacer_login')



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