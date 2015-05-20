# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import RadioSelect

from .models import *
from usuarios.models import Usuario

class EdificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_proyecto',)

    # Solo superuser puede ver modelos edificacion en el admin
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
    # Solo superuser puede ver modelos edificacion en el admin
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class InformacionFinancieraAdmin(admin.ModelAdmin):
    list_display = ('edificacion', 'dinero_efectivo', 'valor_terreno', 'valor_solicitado', 
        'costo_total', 'mano_obra', 'valor_materiales',)

class ComunidadAdmin(admin.ModelAdmin):
    list_display = ('edificacion', 'nombre', 'poblacion_comunidad', 'region', 
        'capital_depto', 'distancia_capital',)

class CongregacionAdmin(admin.ModelAdmin):  
    list_display = ('edificacion', 'nombre', 'fecha_fundacion','region', 'asistencia_general', 
        'asistencia_ninos', 'miembros_adultos', 'miembros_ninos', 'ingreso_mensual',
        'nombre_pastor',)

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

class AdjuntosAdmin(admin.ModelAdmin):
    list_display = ('edificacion', 'foto_construccion', 'foto_congregacion','foto_pastor', 'permiso_construccion', 
        'escritura_terreno', 'plan_terreno', 'plan_construccion', 'historia_congregacion', 'testimonio_pastor',)
        
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'edificacion', 'commenter', 'descripcion')

admin.site.register(Edificacion, EdificacionAdmin)
# admin.site.register(InformacionFinanciera, InformacionFinancieraAdmin)
# admin.site.register(Comunidad, ComunidadAdmin)
# admin.site.register(Congregacion, CongregacionAdmin)
# admin.site.register(Fuentes_Financiacion)
# admin.site.register(Condiciones, CondicionesAdmin)
# admin.site.register(Adjuntos, AdjuntosAdmin)
# admin.site.register(Comentario, ComentarioAdmin)
