# -*- coding: utf-8 -*-
from django import forms

from db.models import Edificacion, Comunidad, Congregacion, Fuentes_Financieras, Condiciones


class EdificacionForm(forms.ModelForm):
     class Meta:
         model = Edificacion
         exclude = ['estado']

class ComunidadForm(forms.ModelForm):
     class Meta:
         model = Comunidad
         exclude = ['edificacion']

class CongregacionForm(forms.ModelForm):
     class Meta:
         model = Congregacion
         exclude = ['edificacion']

class FuentesFinancierasForm(forms.ModelForm):
     class Meta:
         model = Fuentes_Financieras
         exclude = ['edificacion']

class CondicionesForm(forms.ModelForm):
     class Meta:
         model = Condiciones
         exclude = ['edificacion']