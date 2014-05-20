# -*- coding: utf-8 -*-
from django import forms

from db.models import Edificacion, Comunidad, Congregacion, Fuentes_Financieras, Condiciones


class EdificacionForm(forms.ModelForm):
     class Meta:
         model = Edificacion

class ComunidadForm(forms.ModelForm):
     class Meta:
         model = Comunidad

class CongregacionForm(forms.ModelForm):
     class Meta:
         model = Congregacion

class FuentesFinancierasForm(forms.ModelForm):
     class Meta:
         model = Fuentes_Financieras

class CondicionesForm(forms.ModelForm):
     class Meta:
         model = Condiciones