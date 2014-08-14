# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import RadioSelect

from leaflet.admin import LeafletGeoAdmin
from .models import *


class CondicionesAdmin(admin.ModelAdmin):
    radio_fields = {
        'construccion': admin.VERTICAL,
        'mantenimiento': admin.VERTICAL,
        'actividades': admin.VERTICAL,
        'discipulado': admin.VERTICAL,
        'alcance': admin.VERTICAL,
        'found_trust': admin.VERTICAL,
        'found_commitment': admin.VERTICAL,
        'presupuesto': admin.VERTICAL,
        'terminacion': admin.VERTICAL,
    }

    fieldsets = ( 
        (None, {
            'fields': ('edificacion',)
        }),
        ('Reportar progreso de construcción', {
            'fields': ('construccion',)
        }),
        ('Mantenimiento del edificio', {
            'fields': ('mantenimiento',)
        }),
        ('Reporte de Actividades', {
            'fields': ('actividades',)
        }),
        ('Discipular Creyentes / Materiales de estudio bíblico', {
            'fields': ('discipulado',)
        }),
        ('Alcance y Plantación de Iglesias Hijas', {
            'fields': ('alcance',)
        }),
        ('Pacto de Fondos de la Iglesia', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('found_trust', 'found_commitment', 'found_payment')
        }),
        ('Presupuesto del Proyecto', {
            'fields': ('presupuesto',)
        }),
        ('Terminación del Proyecto', {
            'fields': ('terminacion',)
        }),
        ('Comentarios Adiccionales', {
            'fields': ('comentarios',)
        }),    
        ('Firma Electrónica (Aceptación de los términos y condiciones de ICM)', {
            'fields': ('aceptacion', 'nombre_completo')
        }),
    )
        

admin.site.register(Edificacion, LeafletGeoAdmin)
admin.site.register(Comunidad)
admin.site.register(Fuentes_Financiacion)
admin.site.register(Condiciones, CondicionesAdmin)
admin.site.register(Adjuntos)


