# -*- coding: utf-8 -*-
from django import forms

from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons

from db.models import Edificacion, Comunidad, Congregacion, Fuentes_Financieras, Condiciones
from .datos import EDIFICACION_COORDENADAS

class EdificacionForm(forms.ModelForm):

    coordenadas = PointField(help_text=EDIFICACION_COORDENADAS)

    class Meta:
        model = Edificacion
        exclude = ['estado']
        #widgets = {'coordenadas': LeafletWidget()}

    def __init__(self, *args, **kwargs):
        super(EdificacionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        #self.fields['coordenadas'].label = False
        self.fields['coordenadas'].field_class = 'col-sm-12'

        self.helper.layout = Layout(
            Field('nombre_proyecto', css_class='input-sm'),
            Field('direccion', rows="2", css_class='input-xlarge', wrapper_class="hoajajajjaj"),          
            Field('coordenadas', css_class="col-sm-12"),

            Fieldset(
                'Propiedad de la tierra donde se construira el proyecto',
                Field('owner_escritura', css_class='input-sm'),
                Field('tipo_adquisicion', css_class='input-sm'),
                Field('tiempo_limite', css_class='input-sm'),  # dudas con el tipo de campo 
                Field('dimensiones_terreno', css_class='input-sm'),
                Field('dimensiones_edificio', css_class='input-sm'),
                Field('tipo_construccion', css_class='input-sm'),
                Field('metodo_construccion', css_class='input-sm'),
                Field('requiere_permiso', css_class='input-sm'),
                Field('is_icm_approved', css_class='input-sm'),
                Field('moneda_local', css_class='input-sm'),
                Field('requiere_permiso', css_class='input-sm'),
                Field('dolar_moneda_local', css_class='input-sm'),
            ),

            Fieldset(
                'Informacion Financiera',
                Field('labor_moneda_local', css_class='input-sm'),
                Field('labor_dolares', css_class='input-sm'),
                Field('materiales_moneda_local', css_class='input-sm'),  # dudas con el tipo de campo 
                Field('materiales_dolares', css_class='input-sm'),
                Field('dinero_moneda_local', css_class='input-sm'),
                Field('dinero_dolares', css_class='input-sm'),
                Field('terreno_moneda_local', css_class='input-sm'),
                Field('terreno_dolares', css_class='input-sm'),
                Field('valor_solicitado_monedalocal', css_class='input-sm'),
                Field('valor_solicitado_dolares', css_class='input-sm'),
                Field('costo_total_monedalocal', css_class='input-sm'),
                Field('costo_total_dolares', css_class='input-sm'),
                Field('pago_fondo', css_class='input-sm'),        
            ),

            'estado',  # este estado debe manejar mas de dos tipos,, por ejempo, uno por cada form y otro cuando fue envidado

        )

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
