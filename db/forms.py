# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons, UneditableField

from db.models import Edificacion, Comunidad, Congregacion, Adjuntos, Condiciones, InformacionFinanciera, Fuentes_Financiacion, Comentario
from .datos import EDIFICACION_COORDENADAS

from map_field import widgets as map_widgets
from map_field import fields as map_fields

class ModelFormBase(forms.ModelForm):
            
    def quien_soy(self):
        return self.instance

class EdificacionForm(ModelFormBase):  

    class Meta:
        model = Edificacion
        exclude = ['estado', 'usuario', 'etapa_actual', 'ingeniero', 'arquitecto', 
                    'aprobacion_regional', 'aprobacion_arquitecto', 
                    'aprobacion_ingeniero', 'aprobacion_nacional']

    def __init__(self, *args, **kwargs):
        super(EdificacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_class       = 'form-horizontal'
        self.helper.form_tag         = False
        self.helper.label_class      = 'col-sm-3'
        self.helper.field_class      = 'col-sm-9'
        self.fields['coordenadas'].widget = map_widgets.MapsGeoPointhWidget()

        # Esta es una manera mas sencilla de agregar atributos a los campos
        self.helper.all().wrap(Field, css_class='input-sm') 
        self.helper['direccion'].wrap(Field, css_class="input-xlarge", rows="2")
        self.helper['coordenadas'].wrap(Field, css_class="geolocation_field")
        #self.helper['requiere_permiso'].wrap(Field, css_class="col-sm-offset-2")
        #self.helper.filter_by_widget(forms.Select).wrap(Field, css_class='select select-primary mbl') 



class InformacionFinancieraForm(ModelFormBase):
    
    class Meta:
        model = InformacionFinanciera
        exclude = ['edificacion', 'mano_obra', 'valor_materiales']

    def __init__(self, *args, **kwargs):
        super(InformacionFinancieraForm, self).__init__(*args, **kwargs)        
        self.helper = FormHelper(self)

        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        #self.fields['valor_solicitado'].widget.attrs['disabled'] = True

        self.helper.all().wrap(Field, css_class='input-sm') 
        self.helper.filter_by_widget(forms.Select).wrap(Field, css_class='select select-primary mbl') 


class ComunidadForm(ModelFormBase):
    
    class Meta:
        model = Comunidad
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(ComunidadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.helper.all().wrap(Field, css_class='input-sm')

class CongregacionForm(ModelFormBase):
    
    class Meta:
        model = Congregacion
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CongregacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.helper.all().wrap(Field, css_class='input-sm')
        self.helper.filter_by_widget(forms.Select).wrap(Field, css_class='select select-primary mbl') 
        self.helper.filter_by_widget(forms.Textarea).wrap(Field, css_class="input-xlarge", rows="2") 

class CondicionesForm(ModelFormBase):
    
    class Meta:
        model = Condiciones
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CondicionesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'

        self.helper.all().wrap(Field, css_class='input-sm')
        self.helper.filter_by_widget(forms.Select).wrap(Field, css_class='select select-primary mbl') 
        self.helper.filter_by_widget(forms.Textarea).wrap(Field, css_class="input-xlarge", rows="4") 

class AdjuntosForm(ModelFormBase):
    
    class Meta:
        model = Adjuntos
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(AdjuntosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag     = False
        self.helper.label_class  = 'col-sm-3'
        self.helper.field_class  = 'col-sm-9'


class FuentesFinanciacionForm(forms.ModelForm):
    
    class Meta:
        model = Fuentes_Financiacion
        exclude = ['info_financiera']

    def __init__(self, *args, **kwargs):
        super(FuentesFinanciacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
    
class ComentarioForm(forms.ModelForm):
    """Formulario para crear un comentario"""
    
    class Meta:
        model = Comentario
        exclude = ['edificacion', 'commenter', 'created']

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_show_labels = False

        self.helper.layout = Layout(
            PrependedText('descripcion', "<i class='fa fa-user '></i>", placeholder="Agrega tu comentario", rows="1", ng_focus="procesarFoco($event)", ng_blur="procesarFoco($event)"),
            FormActions(
                Submit('Submit', 'Enviar', css_class='btn-info pull-right btn-xs', ng_show="verSubmit")
            )
        )

