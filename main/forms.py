# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons


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
    


class LoginForm(AuthenticationForm):
  
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()

		self.helper.form_show_labels = False

		self.helper.layout = Layout(
			PrependedText('username', "@", css_class="input-sm", placeholder="email"),
			PrependedText('password', "<i class='fa fa-key'></i>", css_class="input-sm", placeholder="password"),
			FormActions(
	            Submit('entrar', 'Entrar', css_class="btn-success btn-block"),
	        )
		)
	

