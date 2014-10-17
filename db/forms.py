# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons

from db.models import Edificacion, Comunidad, Congregacion, Adjuntos, Condiciones, InformacionFinanciera, Fuentes_Financiacion, Comentario
from .datos import EDIFICACION_COORDENADAS

from map_field import widgets as map_widgets
from map_field import fields as map_fields

class ModelFormBase(forms.ModelForm):
            
    def quien_soy(self):
        return self.instance

class EdificacionForm(ModelFormBase):  

    #coordenadas = forms.CharField(widget=map_widgets.MapsGeoPointhWidget()) 

    class Meta:
        model = Edificacion
        exclude = ['estado', 'usuario', 'etapa_actual']

    def __init__(self, *args, **kwargs):
        super(EdificacionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        #self.fields['coordenadas'].label = False
        self.fields['coordenadas'].widget = map_widgets.MapsGeoPointhWidget()
        #self.fields['coordenadas'].field_class = 'col-sm-12'

        self.helper.layout = Layout(
            Field('nombre_proyecto', css_class='input-sm'),
            Field('direccion', rows="2", css_class='input-xlarge', wrapper_class="hoajajajjaj"),          
            Field('coordenadas', css_class="col-sm-12 input-sm geolocation_field"),

            Fieldset(
                'Propiedad de la tierra donde se construira el proyecto',
                Field('owner_lote', css_class='input-sm'),
                Field('tipo_adquisicion', css_class='input-sm'),
                Field('dimensiones_terreno', css_class='input-sm'),
                Field('dimensiones_edificio', css_class='input-sm'),
                Field('num_pisos', css_class='input-sm'),                
                Field('tipo_construccion', css_class='input-sm'),
                Field('metodo_construccion', css_class='input-sm'),
                Field('requiere_permiso', css_class='input-sm'),
                Field('tiempo_limite', css_class='input-sm'),
            ),
        )
from crispy_forms.bootstrap import UneditableField
class InformacionFinancieraForm(ModelFormBase):
    class Meta:
        model = InformacionFinanciera
        exclude = ['edificacion', 'mano_obra', 'valor_materiales']

    def __init__(self, *args, **kwargs):
        super(InformacionFinancieraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        #self.fields['valor_solicitado'].widget.attrs['disabled'] = True


class ComunidadForm(ModelFormBase):
    class Meta:
        model = Comunidad
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(ComunidadForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

class CongregacionForm(ModelFormBase):
    class Meta:
        model = Congregacion
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CongregacionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

class CondicionesForm(ModelFormBase):
    class Meta:
        model = Condiciones
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CondicionesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

class AdjuntosForm(ModelFormBase):
    class Meta:
        model = Adjuntos
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(AdjuntosForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

class FuentesFinanciacionForm(forms.ModelForm):
    class Meta:
        model = Fuentes_Financiacion
        exclude = ['info_financiera']

    def __init__(self, *args, **kwargs):
        super(FuentesFinanciacionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
    
class ComentarioForm(forms.ModelForm):
    """Formulario para crear un comentario"""
    
    class Meta:
        model = Comentario
        exclude = ['edificacion', 'commenter']

           