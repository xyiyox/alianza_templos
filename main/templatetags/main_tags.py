# -*- coding: utf-8 -*-
from django import template
from django.utils.timesince import timesince
from db.models import Etapa
import os

register = template.Library()

@register.filter
def percent_to_color(percent):
	if percent < 90:
		return 'success'
	elif percent <= 100:
		return 'warning'
	else:
		return 'danger'


@register.filter
def percent_to_msg(percent, plazo):
	if percent <= 100:
		return '%s%s' %(percent, '%')
	else:
		return 'plazo vencido hace %s' %timesince(plazo)


@register.filter
def etapa_to_icon(etapa):

	for key, value in Etapa.ETAPA_ACTUAL:
		if etapa == key:
			return Etapa.ICONS[key-1]
	
	return "home"


@register.filter
def etapa_to_general_progress(etapa):
	#return (etapa * 100) / len(Etapa.ETAPA_ACTUAL)
	return int( (etapa * 100) / Etapa.DEDICACION )


@register.filter
def create_key(type,step):	
	return 'CAD_{}{}'.format(type, step)

@register.filter
def key_print(list, key_name):
    return list[key_name]	

@register.filter
def extencion(name):	
	ext = os.path.splitext(name)[1]	
	if ext == '.jpg' or ext == '.png' or ext == '.jpeg':
		return True
	else:
		return False

@register.filter
def extencion(name):	
	ext = os.path.splitext(name)[1]	
	if ext == '.jpg' or ext == '.png' or ext == '.jpeg':
		return True
	else:
		return False

@register.filter
def terreno(name):		
	if name == 0 :
		return 'Plano'
	else:
		return 'Desnivel'

@register.filter
def localidad(name):		
	if name == 0 :
		return 'Rural'
	elif name == 1:
		return 'Urbano'
	else:
		return 'Veredal'

@register.filter
def vecinos(name):		
	if name == 0 :
		return 'Izquierda'
	elif name == 1:
		return 'Derecha'
	elif name == 2:
		return 'Atras'	
	else:
		return 'Der/Izq'

@register.filter
def ubicacion(name):		
	if name == 0 :
		return 'Esquina Derecha'
	elif name == 1:
		return 'Esquina Izquierda'
	else:
		return 'En la Mitad'

@register.filter
def cuenta(name):		
	if name == 0 :
		return 'Ahorros'
	else:
		return 'Corriente'

@register.filter
def construccion(name):		
	if name == 0 :
		return 'Templo'
	elif name == 1:
		return 'Obra Social'
	elif name == 2:
		return 'Templo/Obra Social (Arriba)'	
	elif name == 3:
		return 'Templo/Obra Social (Lateral Izq)'	
	elif name == 4:
		return 'Templo/Obra Social (Atras)'	
	else:
		return 'Templo/Obra Social (Lateral Der)'

@register.filter
def permiso(name):		
	if name == 0 :
		return 'Curaduria'
	elif name == 1:
		return 'Planeacion'
	else:
		return 'No'