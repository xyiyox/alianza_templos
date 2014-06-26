# -*- coding: utf-8 -*-
from django import forms

from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons

from db.models import Edificacion, Comunidad, Congregacion, Fuentes_Financieras, Condiciones, InformacionFinanciera
from .datos import EDIFICACION_COORDENADAS

class EdificacionForm(forms.ModelForm):   

    class Meta:
        model = Edificacion
        exclude = ['estado']
        #widgets = {'coordenadas': LeafletWidget()}

    coordenadas = PointField(help_text=EDIFICACION_COORDENADAS)

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
                Field('dimensiones_terreno', css_class='input-sm'),
                Field('dimensiones_edificio', css_class='input-sm'),
                Field('tipo_construccion', css_class='input-sm'),
                Field('metodo_construccion', css_class='input-sm'),
                Field('requiere_permiso', css_class='input-sm'),
                Field('is_icm_approved', css_class='input-sm'),
                Field('moneda_local', css_class='input-sm'),
                Field('tiempo_limite', css_class='input-sm'),
            ),
        )
    
    def __unicode__(self):
        return "Edificación"

class InformacionFinancieraForm(forms.ModelForm):
    class Meta:
        model = InformacionFinanciera
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(InformacionFinancieraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.helper.layout = Layout(
            Fieldset(
                'Informacion Financiera',
                Field('mano_obra', css_class='input-sm'),
                Field('valor_materiales', css_class='input-sm'), 
                Field('dinero_efectivo', css_class='input-sm'),
                Field('aporte_terreno', css_class='input-sm'),
                Field('valor_solicitado', css_class='input-sm'),
                Field('costo_total', css_class='input-sm'),
                Field('pago_fondo', css_class='input-sm'),        
            ),
        )

    def __unicode__(self):
        return "Información Financiera"

class ComunidadForm(forms.ModelForm):
    class Meta:
        model = Comunidad
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(ComunidadForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

    def __unicode__(self):
        return "Comunidad"

class CongregacionForm(forms.ModelForm):
    class Meta:
        model = Congregacion
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CongregacionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

    def __unicode__(self):
        return "Congregación"

class FuentesFinancierasForm(forms.ModelForm):
    class Meta:
        model = Fuentes_Financieras
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(FuentesFinancierasForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

    def __unicode__(self):
        return "Fuentes Financieras"

class CondicionesForm(forms.ModelForm):
    class Meta:
        model = Condiciones
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CondicionesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

    def __unicode__(self):
        return "Condiciones"
