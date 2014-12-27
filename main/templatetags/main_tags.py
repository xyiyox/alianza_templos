# -*- coding: utf-8 -*-
from django import template
from django.utils.timesince import timesince
from db.models import Etapa


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
	return (etapa * 100) / len(Etapa.ETAPA_ACTUAL)
