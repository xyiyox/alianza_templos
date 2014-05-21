# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons

from db.models import Edificacion, Comunidad, Congregacion, Fuentes_Financieras, Condiciones


class EdificacionForm(forms.ModelForm):

    class Meta:
        model = Edificacion
        exclude = ['estado']

    def __init__(self, *args, **kwargs):
        super(EdificacionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.form_show_labels = True

        self.helper.form_tag = False

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
