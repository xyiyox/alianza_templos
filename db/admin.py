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
  

admin.site.register(Edificacion, EdificacionAdmin)

