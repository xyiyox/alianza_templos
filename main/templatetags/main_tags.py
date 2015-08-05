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
	return (etapa * 100) / Etapa.DEDICACION


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