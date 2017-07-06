# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, Button, Row, Field, Hidden, MultiField
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons, UneditableField, InlineRadios, InlineCheckboxes, PrependedAppendedText

from db.models import Edificacion, Comunidad, Congregacion, Adjuntos, Condiciones, InformacionFinanciera, Comentario, InformeSemestral, InformeSemestralPublico
from .datos import EDIFICACION_COORDENADAS

from map_field import widgets as map_widgets
from map_field import fields as map_fields
from usuarios.models import Usuario
from django.core.exceptions import ValidationError 


class ModelFormBase(forms.ModelForm):
            
    def quien_soy(self):
        return self.instance

class EdificacionForm(ModelFormBase):  

    class Meta:
        model = Edificacion
        exclude = ['estado', 'usuario', 'etapa_actual', 'ingeniero', 'arquitecto', 'tesorero',
                    'aprobacion_regional', 'aprobacion_arquitecto', 
                    'aprobacion_ingeniero', 'aprobacion_nacional', 'aprobacion_tesorero', 'created', 'updated', 
                    'requiere_arquitecto','aprobacion_internacional', 'usuarios_asignados', 'planos_creados','aprobacion_fotos','envio_icm','envio_alianza','fecha_aprox_dedicacion']

    def __init__(self, *args, **kwargs):
        super(EdificacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_class       = 'form-horizontal'
        self.helper.form_tag         = False
        self.helper.label_class      = 'col-sm-3'
        self.helper.field_class      = 'col-sm-9'
        self.fields['coordenadas'].widget = map_widgets.MapsGeoPointhWidget()
        
        #Esta es una manera mas sencilla de agregar atributos a los campos
        self.helper.all().wrap(Field, css_class='input-sm') 
        self.helper['direccion'].wrap(Field, css_class="input-xlarge", rows="2")
        self.helper['coordenadas'].wrap(Field, css_class="geolocation_field")
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios) 


class InformacionFinancieraForm(ModelFormBase):
    
    class Meta:
        model = InformacionFinanciera
        exclude = ['edificacion']
                    

    def __init__(self, *args, **kwargs):
        super(InformacionFinancieraForm, self).__init__(*args, **kwargs)        
        self.helper = FormHelper(self)

        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.helper.all().wrap(Field, css_class='input-sm') 
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios)

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

        self.fields['fecha_fundacion'].widget = SelectDateWidget(years=( range(1900, date.today().year + 1) ) )
       
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.fields['titulos_obtenidos'].widget = forms.TextInput(attrs={'placeholder': 'Tecnico en Biblia, Master en Biblia'})
      
        self.helper.all().wrap(Field, css_class='input-sm')
        self.helper.filter_by_widget(forms.Textarea).wrap(Field, css_class="input-xlarge", rows="2") 
        self.helper.filter_by_widget(SelectDateWidget).wrap(Field, css_class="input-sm", style="width:110px; float:left; margin-right:5px;") 
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios)
        #self.fields['titulos_obtenidos'].widget = FilteredSelectMultiple("verbose name", is_stacked=False)

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
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios)
        self.helper.filter_by_widget(forms.Textarea).wrap(Field, css_class="input-xlarge", rows="4") 

class AdjuntosForm(ModelFormBase):
    
    class Meta:
        model = Adjuntos
        exclude = ['edificacion', 'planos_arquitecto', 'planos_ingeniero','fotos_p1','fotos_p2','fotos_p3','dedicacion']

    def __init__(self, *args, **kwargs):
        super(AdjuntosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag     = False
        self.helper.label_class  = 'col-sm-3'
        self.helper.field_class  = 'col-sm-9'


    
class ComentarioForm(forms.ModelForm):
    """Formulario para crear un comentario"""
    
    class Meta:
        model = Comentario
        exclude = ['edificacion', 'commenter', 'created']

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_show_labels = False
        self.helper.form_id = 'comentario-form'
        self.helper.form_class = 'clearfix'


        self.helper.layout = Layout(
            PrependedText('descripcion', "<i class='fa fa-user '></i>", placeholder="Agrega tu comentario", rows="1", ng_focus="procesarFoco($event)", ng_blur="procesarFoco($event)"),
            Field('comentario_padre', type="hidden"),
            FormActions(
                StrictButton('Enviar', type="Submit", css_class="btn-info pull-right btn-xs", ng_show="verSubmit", ng_click="alClickComentario($event)", data_loading_text="Enviando...", autocomplete="off"),
            )
        )


    
class InformeSemestralForm(forms.ModelForm):
    """Formulario para crear un comentario"""

    class Meta:
        model = InformeSemestral
        exclude = ['edificacion','fecha_elaboracion','informe']

    def __init__(self, *args, **kwargs):
        super(InformeSemestralForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_show_labels = True
        self.helper.form_class       = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'
        self.helper.form_action = "."

        self.helper.all().wrap(Field, css_class='input-sm')       
        self.helper.filter_by_widget(forms.Textarea).wrap(Field, css_class="input-xlarge", rows="3")

        self.helper.layout = Layout(  
            
            MultiField(
                '<b>Plantación*</b>', 
                Div(
                    HTML('<p class="help-block">Cuantos proyectos misioneros o igleisas hijas fueron plantadas en el ultimo semestre</p>'),
                    Field('plantacion_nombre_1', css_class='input-sm', placeholder="nombre"),  
                    Field('plantacion_lugar_1', css_class='input-sm', placeholder="lugar"),
                    Field('plantacion_fecha_1', css_class='input-sm', placeholder="mes/año"),
                    css_class = 'informe-semestral-plantacion clearfix',
                ),
                Div(
                    Field('plantacion_nombre_2', css_class='input-sm', placeholder="nombre"),  
                    Field('plantacion_lugar_2', css_class='input-sm', placeholder="lugar"),
                    Field('plantacion_fecha_2', css_class='input-sm', placeholder="mes/año"),
                    css_class = 'informe-semestral-plantacion clearfix',
                ),
                Div(
                    Field('plantacion_nombre_3', css_class='input-sm', placeholder="nombre"),  
                    Field('plantacion_lugar_3', css_class='input-sm', placeholder="lugar"),
                    Field('plantacion_fecha_3', css_class='input-sm', placeholder="mes/año"),
                    css_class = 'informe-semestral-plantacion clearfix',
                )
            ),

            Field('miembros_actuales'),
            Field('nuevos_miembros'),
            Field('conversiones'),
            Field('bautismos_nuevos'),
            Field('no_bautismos'),
            Field('asistencia_general'),
            Field('ofrendas'),
            Field('plantacion'),
            Field('grupos_vida'), 
            Field('asistencia_grupos'),
            Field('peticiones_oracion'),
            Field('testimonios'),
            Field('ministerio_ninos'),
            Field('uso_local'),
            Field('fotos'),
            FormActions(      
                
                StrictButton('Enviar Informe', type="Submit", css_class="btn btn-success pull-right btn-md", autocomplete="off"),
            )
        ) 


""" FORMULARIOS AUTORIZACION """

class AprobacionForm(forms.Form):  
    aprobar = forms.CharField(initial='True')

    def __init__(self, *args, **kwargs):
        super(AprobacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(
            Field('aprobar', type='hidden'),
            FormActions(
                StrictButton('Revisar de nuevo', id="revisar-aprobacion-btn", type="button", css_class="btn btn-default", data_dismiss="modal"),
                StrictButton('Estoy seguro', id="submit-aprobacion-btn", type="Submit", css_class="btn btn-primary", 
                    data_loading_text="<i class='fa fa-spinner fa-spin'></i> Procesando...", ng_click="alClickAprobacion()"),
            )
        )


class AprobacionInternacionalForm(ModelFormBase):  
    class Meta:
        model = Edificacion
        fields = ['aprobacion_internacional']         

def validate_planos(value):
    print('Aqui estoy')
    if value != None:       
        raise ValidationError(u'Debe subir planos para poder aprobar')


class PlanosArquitectoForm(ModelFormBase):
    class Meta:
        model = Adjuntos
        fields = ['planos_arquitecto']

    def __init__(self, *args, **kwargs):
        super(PlanosArquitectoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(
            Hidden('planos', Usuario.ARQUITECTO),
            Field('planos_arquitecto'),
            FormActions(
                StrictButton('Subir', type="Submit", css_class="btn btn-primary btn-xs"),
            )
        )

class PlanosIngenieroForm(ModelFormBase):
    class Meta:
        model = Adjuntos
        fields = ['planos_ingeniero']

    def __init__(self, *args, **kwargs):
        super(PlanosIngenieroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(
            Hidden('planos', Usuario.INGENIERO),
            Field('planos_ingeniero'),
            FormActions(
                StrictButton('Subir', type="Submit", css_class="btn btn-primary btn-xs"),
            )
        )


class FotosPAForm(ModelFormBase):
    class Meta:
        model = Adjuntos
        fields = ['fotos_p1']

    def __init__(self, *args, **kwargs):
        super(FotosPAForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(    
            Field('fotos_p1'),
            FormActions(
                StrictButton('Subir', type="Submit", css_class="btn btn-primary btn-xs"),
            )
        )

class FotosPBForm(ModelFormBase):
    class Meta:
        model = Adjuntos
        fields = ['fotos_p2']

    def __init__(self, *args, **kwargs):
        super(FotosPBForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(                    
            Field('fotos_p2'),
            FormActions(
                StrictButton('Subir', type="Submit", css_class="btn btn-primary btn-xs"),
            )
        )  

class FotosPCForm(ModelFormBase):
    class Meta:
        model = Adjuntos
        fields = ['fotos_p3']

    def __init__(self, *args, **kwargs):
        super(FotosPCForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(                 
            Field('fotos_p3'),
            FormActions(
                StrictButton('Subir', type="Submit", css_class="btn btn-primary btn-xs"),
            )
        )

class DedicacionForm(ModelFormBase):
    class Meta:
        model = Adjuntos
        fields = ['dedicacion']

    def __init__(self, *args, **kwargs):
        super(DedicacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(        
            Field('dedicacion'),
            FormActions(
                StrictButton('Subir', type="Submit", css_class="btn btn-primary btn-xs"),
            )
        )
class AprobacionTesoreroForm(ModelFormBase):  
    class Meta:
        model = Edificacion
        fields = ['aprobacion_tesorero']

class AprobacionNacionalForm(ModelFormBase):  
    class Meta:
        model = Edificacion
        fields = ['aprobacion_nacional']


""" FORMULARIOS ASIGNACION Y EDICCION DE USUARIOS """

class AsignarUsuariosForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(AsignarUsuariosForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"

        self.fields['arquitecto'].queryset = Usuario.objects.filter(tipo=Usuario.ARQUITECTO)
        self.fields['ingeniero'].queryset = Usuario.objects.filter(tipo=Usuario.INGENIERO)
        self.fields['tesorero'].queryset = Usuario.objects.filter(tipo=Usuario.TESORERO)

        self.helper.layout = Layout(
            PrependedAppendedText('arquitecto', "<i class='fa fa-user fa-fw'></i>", "arquitecto <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            PrependedAppendedText('ingeniero', "<i class='fa fa-user fa-fw'></i>", "dir. obra <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            PrependedAppendedText('tesorero', "<i class='fa fa-user fa-fw'></i>", "tesorero <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Guardar usuarios', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['arquitecto', 'ingeniero', 'tesorero']


class ArquitectoEditForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(ArquitectoEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"  # es reemplazado en la vista

        self.fields['arquitecto'].queryset = Usuario.objects.filter(tipo=Usuario.ARQUITECTO)
        self.fields['arquitecto'].empty_label = None

        self.helper.layout = Layout(
            Hidden('editar', Usuario.ARQUITECTO),
            PrependedAppendedText('arquitecto', "<i class='fa fa-user fa-fw'></i>", "arquitecto <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Cambiar arquitecto', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['arquitecto']

class IngenieroEditForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(IngenieroEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"  # es reemplazado en la vista

        self.fields['ingeniero'].queryset = Usuario.objects.filter(tipo=Usuario.INGENIERO)
        self.fields['ingeniero'].empty_label = None

        self.helper.layout = Layout(
            Hidden('editar', Usuario.INGENIERO),
            PrependedAppendedText('ingeniero', "<i class='fa fa-user fa-fw'></i>", "dir. obra <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Cambiar dir. de obra', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['ingeniero']


class TesoreroEditForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(TesoreroEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"  # es reemplazado en la vista

        self.fields['tesorero'].queryset = Usuario.objects.filter(tipo=Usuario.TESORERO)
        self.fields['tesorero'].empty_label = None

        self.helper.layout = Layout(
            Hidden('editar', Usuario.TESORERO),
            PrependedAppendedText('tesorero', "<i class='fa fa-user fa-fw'></i>", "tesorero <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Cambiar tesorero', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['tesorero']

class InformeSemestralPublicoForm(forms.ModelForm):
    """Formulario para informe semestral publico sin loguin"""

    class Meta:
        model = InformeSemestralPublico
        exclude = []

    def __init__(self, *args, **kwargs):
        super(InformeSemestralPublicoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class       = 'form-horizontal'

        self.helper.label_class      = 'col-sm-2'
        self.helper.field_class      = 'col-sm-9'

        self.helper.all().wrap(Field, css_class='input-sm')

        self.helper.layout = Layout( 
            Fieldset(
                'Datos del Proyecto',
                Field('nombre_proyecto', css_class='input-sm', placeholder='nombre del proyecto'),
                Field('persona', css_class='input-sm', placeholder='persona encargada del proyecto'),
                Field('email', css_class='input-sm'),
                Field('telefono', css_class='input-sm'),
                Field('depto', css_class='input-sm'),
                Field('direccion', css_class="input-xlarge", rows="2", placeholder='dirección del proyecto'),
                Field('region', css_class='input-sm'),
            ),

            Fieldset(
                'Datos del Informe',
                Field('miembros_actuales', css_class='input-sm', placeholder='miembros actuales'),
                Field('nuevos_miembros', css_class='input-sm', placeholder='miembros nuevos'),
                Field('conversiones', css_class='input-sm'),
                Field('bautismos_nuevos', css_class='input-sm'),
                Field('no_bautismos', css_class='input-xlarge', rows="2"),
                Field('asistencia_general', css_class="input-sm",  placeholder='asistencia general'),
                Field('grupos_vida', css_class='input-sm', placeholder='grupos de vida'),
            ),

            MultiField(
                '<b>Plantación*</b>', 
                Div(
                    HTML(u'<p class="help-block">Cuantos proyectos misioneros o iglesias hijas fueron plantadas en el último semestre</p>'),
                    Field('plantacion_nombre_1', css_class='input-sm', placeholder="nombre"),  
                    Field('plantacion_lugar_1', css_class='input-sm', placeholder="lugar"),
                    Field('plantacion_fecha_1', css_class='input-sm', placeholder="mes/año"),
                    css_class = 'col-sm-11 informe-semestral-plantacion clearfix',
                ),
                Div(
                    Field('plantacion_nombre_2', css_class='input-sm', placeholder="nombre"),  
                    Field('plantacion_lugar_2', css_class='input-sm', placeholder="lugar"),
                    Field('plantacion_fecha_2', css_class='input-sm', placeholder="mes/año"),
                    css_class = 'col-sm-11 informe-semestral-plantacion clearfix',
                ),
                Div(
                    Field('plantacion_nombre_3', css_class='input-sm', placeholder="nombre"),  
                    Field('plantacion_lugar_3', css_class='input-sm', placeholder="lugar"),
                    Field('plantacion_fecha_3', css_class='input-sm', placeholder="mes/año"),
                    css_class = 'col-sm-11 informe-semestral-plantacion clearfix',
                )
            ),

            Field('asistencia_grupos', css_class='input-sm'),
            Field('ofrendas', css_class='input-sm'),
            Field('peticiones_oracion', css_class="input-xlarge", rows="3"),
            Field('testimonios', css_class="input-xlarge", rows="3"),
            Field('ministerio_ninos', css_class="input-xlarge", rows="3"),
            Field('uso_local', css_class="input-xlarge", rows="3"),
            Field('fotos'),
            

            FormActions(
                StrictButton('Enviar Informe', type="Submit", css_class="btn-primary btn-block btn-lg"),
            )
        )