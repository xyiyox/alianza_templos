# -*- coding: utf-8 -*-
from django import template
from django.utils.timesince import timesince

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
	print(plazo)
	if percent <= 100:
		return '%s%s' %(percent, '%')
	else:
		return 'plazo vencido hace %s' %timesince(plazo)


	
