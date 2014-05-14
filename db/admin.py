# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import RadioSelect

from leaflet.admin import LeafletGeoAdmin
from .models import *


class PreguntasAdmin(admin.ModelAdmin):
	radio_fields = {
		'construccion': admin.VERTICAL,
		'mantenimiento': admin.VERTICAL,
		'actividades': admin.VERTICAL,
		'discipulado': admin.VERTICAL,
		'alcance': admin.VERTICAL,

	}

	fieldsets = (
        
        ('Reportar progreso de construcción', {'fields': ('construccion',)}),
        ('Mantenimiento del edificio', {'fields': ('mantenimiento',)}),
        ('Reporte de Actividades', {'fields': ('actividades',)}),
        ('Discipular Creyentes / Materiales de estudio bíblico', {'fields': ('discipulado',)}),
        ('Alcance y Plantación de Iglesias Hijas', {'fields': ('alcance',)}),
    )
		

admin.site.register(Edificacion, LeafletGeoAdmin)
admin.site.register(Comunidad)
admin.site.register(Fuentes_Financieras)
admin.site.register(Condiciones)
admin.site.register(Edificacion_Condiciones)
admin.site.register(Preguntas, PreguntasAdmin)

