# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons


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
	

