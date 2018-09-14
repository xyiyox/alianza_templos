# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta

from sorl.thumbnail import ImageField

from .datos import *
from .choices import DEPTOS, CAPITALES
from map_field import fields as map_fields


class Etapa(models.Model):

	PLAZO_VENCIDO = 111

	# set on project creation
	DILIGENCIAMIENTO 	= 1
	# set on project sending only once
	APROB_REGIONAL 		= 2
	ASIGN_USUARIOS 		= 3
	# el arquitecto sube planos y che
	PLANOS 				= 4
	#APROB_INGENIERO 	= 5
	APROB_TESORERO 		= 6
	APROB_NACIONAL 		= 7
	APROB_INTERNACIONAL = 8
	ESPERANDO_CUPO 		= 9
	ESPERANDO_RECURSOS 	= 10

	CONS_P1 = 11 # FIJA
	CONS_P2 = 12 # FIJA
	CONS_P3 = 13 # SOLO TEMPLO OBRA/SOCIAL
	#CONS_P4 = 14 
	DEDICACION = 14 #FIJA
	INFORMES = 15



	ICONS = ['edit', 'check', 'users', 'area-chart', 'anchor', 'dollar', 'thumbs-o-up', 'globe', 'clock-o', 'cogs', 'home', 'home', 'home', 'heart' , 'clock-o']

	ETAPA_ACTUAL = (
		(DILIGENCIAMIENTO, u'Diligenciamiento'),
		# 1 semana para revisar por usuario regional
		(APROB_REGIONAL, u'Aprobación Regional'),
		(ASIGN_USUARIOS, u'Asignación de Usuarios'),
		# 8 dias para subir planos del proyecto de construcción
		(PLANOS, u'Creación de Planos'),
		(APROB_TESORERO, u'Aprobación Tesorero'),
		(APROB_NACIONAL, u'Aprobación Nacional'),
		# 2 semanas para recibir aprobación internacional
		(APROB_INTERNACIONAL, u'Aprobación Internacional'),
		(ESPERANDO_RECURSOS, u'En Espera de Recursos'),
		(CONS_P1, u'Primera Fase de Construccion'),
		(CONS_P2, u'Segunda Fase de Construccion'),
		(CONS_P3, u'Tercera Fase de Construccion'),
		#(CONS_P4, u'Cuarta Fase de Construccion'),
		(DEDICACION, u'Dedicacion'),
		(INFORMES, u'Informes Semestrales'),
	)

	edificacion = models.ForeignKey('Edificacion')
	etapa       = models.IntegerField(max_length=2, choices=ETAPA_ACTUAL)
	
	created     = models.DateTimeField(auto_now_add = True) 

	class Meta:
		get_latest_by = "created"

	def save(self, *args, **kwargs):
		# Aqui ponemos el codigo del trigger -------
		self.edificacion.etapa_actual = self.etapa
		self.edificacion.save(update_fields=['etapa_actual'])
		# fin de trigger ------
		return super(Etapa, self).save( *args, **kwargs)


	def _get_plazo_actual(self):
		#if self.etapa_actual == APROB_REGIONAL:		
		if self.edificacion.etapa_actual > self.ESPERANDO_RECURSOS and self.edificacion.etapa_actual <= self.DEDICACION:
			if self.edificacion.tipo_construccion >= 2 and self.edificacion.etapa_actual == self.CONS_P1:
				return self.created + timedelta(days=60)
			else:
				return self.created + timedelta(days=40)
		else:	
		    return self.created + timedelta(days=8)
	
	plazo = property(_get_plazo_actual)

	# calcular porcentaje de tiempo hasta el plazo

	def _get_porcentaje_plazo(self):
		now = timezone.now()
		if timezone.is_aware(now):
		   now = timezone.localtime(now)		
		if now <= self.plazo:
			# calculamos el cien por ciento
			delta_rango = (self.plazo - self.created).total_seconds() 
			# calculamos el porcentaje completado
			delta_van   = (now - self.created).total_seconds()   
			result      = (abs(delta_van) * 100) / abs(delta_rango)    
			return int(result)

		return self.PLAZO_VENCIDO
	
	percent = property(_get_porcentaje_plazo)


	def __unicode__(self):
		return "%s" % self.id



class Plazo(models.Model):
	""" esta clase le permite abstraer los plazos de cada etapa para 
	ser cambiados a voluntad segun evoluciona al app """

	etapa = models.PositiveSmallIntegerField(unique=True, max_length=2, choices=Etapa.ETAPA_ACTUAL)
	plazo = models.PositiveSmallIntegerField(max_length=4, help_text='plazo en días')

	peso    = models.IntegerField(max_length=2, unique=True)
	updated = models.DateField(auto_now = True)

	def __unicode__(self):
		return "%s  %s dias" %(self.get_etapa_display(), self.plazo)




class Edificacion(models.Model):
    """
    Representacion de un Proyecto de construccion 
    de un templo para una iglesia de la IACYMC
    """

    class Meta:
        verbose_name_plural = "edificaciones"

    TIPO_OWNER_LOTE_CHOICES = (
        (0, 'Propio Iglesia Local'),
        (1, 'Otro'),
    )

    TIPO_ADQUISICION_CHOICES = (
        (0, 'Comprado'),
        (1, 'Donado'),
    )

    TIPO_CONSTRUCCION_CHOICES = (
        (0, 'Templo',),
        (1, 'Obra Social'),
        (2, 'Templo/Obra Social (Arriba)'),
        (3, 'Templo/Obra Social (Lateral Izq)'),
        (4, 'Templo/Obra Social (Atras)'),
        (5, 'Templo/Obra Social (Lateral Der)'),
    )


    TT = True
    FF = False
    REQUIERE_CHOICES = (		 
        (TT, 'Si'),
        (FF, 'No'),
    )


    TIPO_TERRENO_CHOICES = (
        (0, 'Plano'),
        (1, 'Desnivel'),		
    )

    LOCALIDAD_TERRENO = (
        (0, 'Rural'),
        (1, 'Urbano'),
        (2, 'Veredal'),
    )

    VECINOS_TERRENO = (
        (0, 'Izquierda'),
        (1, 'Derecha'),		
        (2, 'Atras'),	
        (3, 'Der/Izq'),
    )

    UBICACION = (
        (0, 'Esquina Derecha'),
        (1, 'Esquina Izquierda'),		
        (2, 'En la Mitad')
    )

    TIPO_DE_PERMISO = (
        (0, 'Curaduria'),
        (1, 'Planeacion'),		
        (2, 'No')
    )

    ESTADO_FORMULARIO = (
        (0, 'EdificacionForm'),
        (1, 'ComunidadForm'),
        (2, 'CongregacionForm'),
        (3, 'FuentesFinancierasForm'),
        (4, 'CondicionesForm'),
        (5, 'Terminado'),
    )	

    nombre_proyecto = models.CharField(max_length=40, verbose_name='Nombre del Proyecto')
    direccion 		= models.TextField(verbose_name='Dirección')
    coordenadas 	= map_fields.GeoLocationField(max_length=100, help_text=EDIFICACION_COORDENADAS) 	
    owner_lote 		= models.SmallIntegerField('Dueño del Lote', choices=TIPO_OWNER_LOTE_CHOICES , default=0)
    tipo_adquisicion = models.SmallIntegerField('Método de Adquisición', choices=TIPO_ADQUISICION_CHOICES , default=0)

    tipo_terreno = models.SmallIntegerField('Estado del Terreno', choices=TIPO_TERRENO_CHOICES , default=0)
    localidad_terreno = models.SmallIntegerField('Localidad del Terreno', choices=LOCALIDAD_TERRENO , default=0)
    vecinos_terreno = models.SmallIntegerField('Vecinos del Terreno', choices=VECINOS_TERRENO , default=0)
    ubucacion_construccion = models.SmallIntegerField('Ubicacion de la Construccion', choices=UBICACION , default=0)
    informacion_adicional = models.TextField('Datos adicionales del Terreno', 
                        help_text='Ingrese informacion adicional sobre el tereno, como desniveles, tipo de lugar, datos adionales que permitan agilizar el proceso de la creacion de los planos.',null=True, blank=True)

    dimensiones_terreno = models.CharField('Dimensiones del Terreno', max_length=30, help_text=
        "Ingrese Ancho x Largo en Metros")
    dimensiones_edificio = models.CharField('Dimensiones del Edificio',max_length=30, help_text=
        "Ingrese las medidas en Metros. Para construcción de templos las médidas autorizadas "
        "son 200 mt cuadrados y para obra social 150 mt cuadrados. Si las médidas superan estos "
        "valores entonces se asume que la congregación aporta el excedente del dinero")

    num_pisos 			= models.SmallIntegerField('Cantidad de Pisos', choices=((1, 1), (2, 2)), default=1 )
    tipo_construccion 	= models.SmallIntegerField('Tipo de Construcción', choices=TIPO_CONSTRUCCION_CHOICES, default=0,help_text=
        "Seleccione el tipo de Construccion, Tenga encuenta para el caso de Templo/Obra Social"
        " de identificar como se va construir esta instalacion, esta informacion es importante y debe ser precisa")
    requiere_permiso 	= models.BooleanField('¿Requiere permiso de construcción?',choices=REQUIERE_CHOICES, default=True)
    tipo_permiso 		= models.SmallIntegerField('Tipo de Permiso',choices=TIPO_DE_PERMISO, default=0)
    tiempo_limite 		= models.PositiveSmallIntegerField('Tiempo Limite', help_text='Tiempo en que se terminará la construcción (Meses), Templo 6 Max Meses, Templo/Obra Max 8 Meses.')
        

    # control de estado y etapa
    estado 			= models.SmallIntegerField(choices=ESTADO_FORMULARIO)
    etapa_actual 	= models.PositiveSmallIntegerField(choices=Etapa.ETAPA_ACTUAL)


    # usuarios involucrados, el nacional y el regional se asignan por defecto
    usuario 	= models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Responsable', 
                    related_name='usuario')
    ingeniero 	= models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Maestro de Obra Asignado', 
                    null=True, blank=True, related_name='ingeniero')
    arquitecto 	= models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Arquitecto Asignado', 
                    null=True, blank=True, related_name='arquitecto')
    tesorero 	= models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Tesorero Asignado', 
                    null=True, blank=True, related_name='tesorero')

	# aprobaciones para cambiar de etapa, estan en orden temporal
    aprobacion_regional 	= models.BooleanField(default=False)
    usuarios_asignados      = models.BooleanField(default=False)

    aprobacion_arquitecto 	= models.BooleanField(default=False)
    aprobacion_ingeniero 	= models.BooleanField(default=False)

    planos_creados          = models.BooleanField(default=False)
    aprobacion_tesorero 	= models.BooleanField(default=False)
    aprobacion_nacional 	= models.BooleanField(default=False)
    aprobacion_internacional= models.BooleanField(default=False)	

    aprobacion_fotos = models.PositiveSmallIntegerField(default=0)# Campo Generico de aprobacion de fotos
    envio_icm        = models.BooleanField(default=False)# Campo Generico de envio de icm a a la alianza
    envio_alianza    = models.BooleanField(default=False)# Campo Generico de envio alianza a la iglesia

    fecha_aprox_dedicacion     = models.DateTimeField(null=True, blank=True)

    created     = models.DateField(auto_now_add =True)
    updated     = models.DateField(auto_now = True)

    icm_pin     = models.CharField(max_length=40, null=True, blank=True, verbose_name='Pin de ICM')

    def __unicode__(self):
        return "%s" %u"Edificación"

    def get_absolute_url(self):
        return reverse('main.views.proyecto', args=[str(self.id)])

    # properties
    def _get_registro_etapa(self):
        return self.etapa_set.latest()

    etapa = property(_get_registro_etapa)


class InformacionFinanciera(models.Model):
	""" Informacion Financiera """

	class Meta:
		verbose_name_plural = "informaciones financieras"

	VALOR_SOLICITADO_CHOICES = (
		(0, 14000),
		(1, 25000),
		(2, 39000),
	)


	TIPO_CUENTA = (
		(0, 'Ahorros'),
		(1, 'Corriente'),	
	)

	TIPO_PAGO_FONDO = (
		(0, 'Cuota Fija Mensual'),
		(1, 'Porcentaje Mensual de Ofrendas'),
	)

	# Contribuciones estimadas de la congregacion
	#mano_obra 			= models.PositiveIntegerField('Costo de la Mano de obra', default=0, blank=True)
	#valor_materiales 	= models.PositiveIntegerField('Costo de Materiales de construcción', default=0, blank=True)
	dinero_efectivo 	= models.PositiveIntegerField('Dinero Ahorrado', 
							help_text='Ingrese el valor en Pesos Colombianos (COP), El total con el que cuenta Fisicamente')
							#. <br>Puede usar '
							#'<a href="http://www.colombia.com/cambio_moneda/" target="_blank">este enlace</a> '
							#'como convertidor de moneda.')
	valor_terreno 		= models.PositiveIntegerField('Valor del Terreno', 
							help_text='Ingrese el valor en Pesos Colombianos (COP)')
	#valor_solicitado 	= models.PositiveIntegerField('Dinero Solicitado', choices= VALOR_SOLICITADO_CHOICES, 
	#						help_text='Recuerde que este dinero esta expresado en Dolares (Estados Unidos)')
	num_voluntarios		= models.PositiveSmallIntegerField('Cantidad de Voluntarios', 
							help_text='¿Cuantas personas tiene disponibles para ayudar fisicamente en la construcción?')
	desc_voluntarios 	= models.TextField('Descripción', 
							help_text='Describa que trabajos pueden hacer los Voluntarios y cuantas horas semanales pueden donar')
	#dias_donados 		= models.PositiveSmallIntegerField('Dias Donados', 
	#						help_text='¿Cuantos dias de trabajo donaran aquellos que no pueden ayudar fisicamente a la obra?', 
	#						null=True, blank=True)
	costo_total 		= models.PositiveIntegerField('Costo total del proyecto', 
							help_text='Ingrese el valor en Pesos Colombianos (COP)')
	
	tipo_cuenta         = models.SmallIntegerField('Tipo de Cuenta', choices=TIPO_CUENTA,default=0)
	titular_cuenta      = models.CharField('Titular', max_length=100,help_text="Debe ser una cuenta de la iglesia",default="")
	banco				= models.CharField('Nombre del Banco', max_length=100,default="")	
	numero_cuenta 		= models.CharField(max_length=40, verbose_name='Numero de Cuenta',help_text='Ingrese el Numero de Cuenta,(Necesario si se aprueba el proyecto para hacer las consignaciones)',default='00-00000-00')
	
	# Relacion 1 a 1 entre la edificacion y la informacion financiera
	edificacion 		= models.OneToOneField('Edificacion')

	def __unicode__(self):
		return "%s" %u"Información Financiera"


class Comunidad(models.Model):
	""" Informacion de la ciudad """

	class Meta:
		verbose_name_plural = "ciudades"

	nombre 				= models.CharField('Nombre', max_length=50)
	poblacion_comunidad = models.CharField('Población', max_length=40, help_text="Cantidad de habitantes en número")
	region 				= models.CharField('Departamento', max_length=30, choices=DEPTOS) 
	capital_depto 		= models.CharField('Capital del Departamento', max_length=30, choices=CAPITALES)
	distancia_capital	= models.PositiveSmallIntegerField('Distancia del Proyecto a la capital', 
							help_text="Por favor ingrese el valor en Kilometros (Km)")
	iglesia_cercana     = models.CharField('Iglesia más cercana', max_length=50, help_text="Iglesia más cercana al proyecto.")
	distancia_iglesia   = models.PositiveSmallIntegerField('Distancia a la Iglesia', help_text="La iglesia más cercana debe estar minimo a 10 o 15 km. (ingrese valor en kilómetros)")
	vereda 				= models.CharField('Vereda', max_length=50,help_text='Ingrese el la Vereda donde se va realizar la construccion, si aplica.',null=True, blank=True) 
	corregimiento 		= models.CharField('Corregimiento', max_length=50,help_text='Ingrese el Corregimiento donde se va realizar la construccion, si aplica.',null=True, blank=True) 
	# Relacion 1 a 1 entre la edificacion y la comunidad
	edificacion 		= models.OneToOneField('Edificacion')

	def __str__(self):
		return "%s" %"Ciudad"

class Congregacion(models.Model):
	""" Informacion de la congregación """

	class Meta:
		verbose_name_plural = "congregaciones"

	REGION_CHOICES = (
		(0, 'Central'),
		(1, 'Sur Oriental'),
		(2, 'Mecusab'),
		(3, 'Pacífico'),
		(4, 'Sur'),
		(5, 'Valle'),
		(6, 'Guanbianos'),
		(7, 'Paez'),
        (8, 'Bautista'),
	)

	ESTADO_CIVIL_CHOICES = (
		(0, 'Soltero'),
		(1, 'Casado'),
		(2, 'Viudo'),
		(3, 'Otro'),
	)

	nombre 				= models.CharField(max_length=30)
	fecha_fundacion 	= models.DateField('Fecha de Fundación de la Congregacion')
	lengua_primaria 	= models.CharField('Lengua Materna', max_length=20)
	region 				= models.SmallIntegerField('Región', choices=REGION_CHOICES,default=0, 
							help_text='La Región a la que pertenece la Iglesia')
	asistencia_general 	= models.SmallIntegerField('Asistencia general promedio', help_text="Incluya adultos y niños.")
	asistencia_ninos 	= models.SmallIntegerField('Asistencia general promedio de niños')
	miembros_adultos 	= models.SmallIntegerField('Cantidad de miembros adultos', 
							help_text='Recuerde que se considera como miembro a aquel que ha sido bautizado')
	miembros_ninos 		= models.SmallIntegerField('Cantidad de miembros niños')
	ingreso_mensual 	= models.DecimalField('Ingreso mensual promedio', max_digits=15, decimal_places=3)

	""" 
	Informacion del Pastor 
	"""
	nombre_pastor 			= models.CharField('Nombre del pastor', max_length=50)

	telefono_pastor 		= models.CharField('Telefono del pastor', max_length=20,null=True, blank=True)
	celular_pastor 			= models.CharField('Celular del pastor', max_length=20, help_text="Si no tiene celular, ponga un número de contacto.")
	email_pastor 			= models.CharField('Email del pastor', max_length=80, help_text="Crear correo electrónico nuevo o poner el mismo de esta cuenta.")

	estado_civil 			= models.SmallIntegerField('Estado civil', choices=ESTADO_CIVIL_CHOICES , default=0)
	cant_hijos 				= models.PositiveSmallIntegerField('Cantidad de hijos')
	entrenamiento_biblico 	= models.PositiveSmallIntegerField('Años de entrenamiento Biblico')
	titulos_obtenidos 		= models.CharField('Titulos obtenidos', max_length=50)
	anios_iglesia 			= models.PositiveSmallIntegerField('Años de servicio en la congregación actual')
	anios_ministerio 		= models.PositiveSmallIntegerField('Años de servicio en el ministerio')

	#hay_material 			= models.BooleanField('¿El pastor conoce el material del Instituto Biblico del Aire?', default=False)
	#q1_why_not 				= models.TextField('¿Por que no?', blank=True, null=True)
	#usa_material			= models.BooleanField('¿El pastor ha acordado usar este material para crecimiento de la iglesia?', default=False) 
	#q2_why_not 				= models.TextField('¿Por que no?', blank=True, null=True)
	#q2_how_do 				= models.TextField('¿Como lo hace?', blank=True, null=True)
	# Relacion 1 a 1 entre la edificacion y la congregacion
	edificacion 			= models.OneToOneField('Edificacion')

	def __str__(self):
		return "%s" %"Congregación"
	
#class FuentesFinanciacion(models.Model):
#	""" 
#	Tabla que almacenara posibles entradas economicas dinstintas a ICM que tenga el proyecto
#	"""
#	nombre 			= models.CharField(max_length=30)
#	valor 			= models.DecimalField('Valor', max_digits=15, decimal_places=3)
#	
#	info_financiera = models.ForeignKey('InformacionFinanciera')

def validate_terminos(value):
	if value != True:
		raise ValidationError(u'Debe aceptar las condiciones antes de continuar')

class Condiciones(models.Model):
	""" Condiciones """

	class Meta:
		verbose_name_plural = "condiciones"

	edificacion       = models.ForeignKey('Edificacion')
	construccion      = models.BooleanField(CONDICIONES_CONSTRUCCION, choices=BOOL_CHOICES, default=False)
	mantenimiento     = models.BooleanField(CONDICIONES_MANTENIMIENTO, choices=BOOL_CHOICES, default=False)
	actividades       = models.BooleanField(CONDICIONES_ACTIVIDADES, choices=BOOL_CHOICES, default=False)
	discipulado       = models.BooleanField(CONDICIONES_DISCIPULADO, choices=BOOL_CHOICES, default=False)
	alcance           = models.BooleanField(CONDICIONES_ALCANCE, choices=BOOL_CHOICES, default=False)
	
	found_commitment  = models.BooleanField('Estoy al dia con el 13%, y me comprometo a mantenerlo durante y despues de la construccion.', choices=BOOL_CHOICES, default=False)

	presupuesto       = models.BooleanField(CONDICIONES_PRESUPUESTO, choices=BOOL_CHOICES, default=False)
	terminacion       = models.BooleanField(CONDICIONES_TERMINACION, choices=BOOL_CHOICES, default=False)
	comentarios       = models.TextField(CONDICIONES_COMENTARIOS, blank=True)
	aceptacion        = models.BooleanField('He leído y estoy de acuerdo con los Términos y Condiciones', 
						help_text=CONDICIONES_ACEPTACION, default=False, validators=[validate_terminos])
	nombre_completo   = models.CharField(max_length=50, help_text=CONDICIONES_FULL_NAME)

	def __str__(self):
		return "%s" %"Condiciones"

def calcular_ruta(self, filename):
	return 'adjuntos/%s/%s' %(self.edificacion.pk, filename)

class Adjuntos(models.Model):
    """ Modelo para almacenar los archivos adjuntos """

    class Meta:
        verbose_name_plural = "adjuntos"

    edificacion   			= models.ForeignKey('Edificacion')

    foto_construccion 		= models.ImageField('Foto del Terreno', upload_to=calcular_ruta,
                                help_text='Mostrando claramente el terreno donde se va a construir la iglesia, jpg o png, minimo 600 x 480 pixeles, Tamaño maximo 2MB')
    foto_congregacion 		= models.ImageField('Foto de la congregación', upload_to=calcular_ruta, 
                                help_text='Mostrando el lugar donde se reunen actualmente')
    foto_pastor 			= models.FileField('Foto del Pastor', upload_to=calcular_ruta,
                                help_text='Incluya una foto del pastor en caso de no aparecer en la foto de la congregación')

    permiso_construccion 	= models.FileField('Permiso de construcción o Certificado de que no necesita Permiso', upload_to=calcular_ruta,
                                help_text='Debe agregar el permiso de construccion, si no necesida debe agregar la prueba de que no necesita permiso.',null=True, blank=True)
    escritura_terreno 		= models.FileField('Escritura del terreno Autenticada, o Promesa de Compra', upload_to=calcular_ruta,
                                help_text='Mostrando la prueba de propiedad')
    manzana_catastral 		= models.FileField('Manzana Catastral o Croquis dibujado a Mano', upload_to=calcular_ruta, help_text='Mostrando las dimensiones de la propiedad y la ubicación de la tierra, Si el instituto Augustin Codaci no le proporciona este documento, puede adjuntar un dibujo de la localizacion(mapa pequeño) de el lugar donde se construira el templo')
    plan_construccion 		= models.FileField('Plan de construcción', upload_to=calcular_ruta, null=True, blank=True,
                                help_text='Obligatorio para todos los planes que no hacen parte de los aprobados por ICM')
    historia_congregacion 	= models.FileField('Historia de la congregación', upload_to=calcular_ruta,
                                help_text='Incluya una breve historia de la congregación preferiblemente en formato WORD.')
    testimonio_pastor 		= models.FileField('Testimonio del pastor', upload_to=calcular_ruta,
                                help_text='Incluya el testimonio del pastor de la congregación preferiblemente en formato WORD.')

    certificacion           = models.FileField('Certificación', upload_to=calcular_ruta, help_text="Agregue certificación bancaria o de materiales")
    planos_arquitecto       = models.FileField('Planos', upload_to=calcular_ruta, null=True, blank=False)
    planos_ingeniero        = models.FileField('Planos', upload_to=calcular_ruta, null=True, blank=False)

    fotos_p1       			= models.FileField('Comprimido de Fotos', upload_to=calcular_ruta, null=True, blank=False)
    fotos_p2        		= models.FileField('Comprimido de Fotos', upload_to=calcular_ruta, null=True, blank=False)
    fotos_p3        		= models.FileField('Comprimido de Fotos', upload_to=calcular_ruta, null=True, blank=False)
    dedicacion      		= models.FileField('Dedicacion Comprimido', upload_to=calcular_ruta, null=True, blank=False)

    def __str__(self):
        return "%s" %"Adjuntos"


class Comentario(models.Model):
	""" Modelo para almacenar los comentarios de una edificacion """
	
	edificacion 		= models.ForeignKey('Edificacion')

	commenter 			= models.ForeignKey(settings.AUTH_USER_MODEL)
	descripcion 		= models.TextField('Comentario')
	comentario_padre 	= models.ForeignKey('Comentario', null=True, blank=True)
	created     		= models.DateTimeField(auto_now_add = True) 


def ruta_fotos_informe_semestral(self, filename):
	return 'adjuntos/%s/informes/%s' %(self.edificacion.pk, filename)

def validate_comprimidos(value):
    # El archivo no debe ser mayor a  50MB - 5242880 
    import os
    max_upload_size = 5242880
    #print "content type"
    #print value.file.content_type da error cuando se guarda desde el admin
    #print "size"
    #print value.file._size
    
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.rar','.zip']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Solo se aceptan archivos en formato comprimido .zip o .rar')

    # if value.file._size > max_upload_size:
    #     raise ValidationError(u'El archivo no debe superar las 50 megas de peso')


class InformeSemestral(models.Model):

    TIPO_PLANTACION_CHOICES = (
		('Grupo de vida', 'Grupo de vida'),
		('Iglesia hija', 'Iglesia hija'),
        ('Proyecto Misionero', 'Proyecto Misionero'),
	)

    """ Modelo para almacenar los comentarios de una edificacion """
    class Meta:
        verbose_name_plural = "informes"

    edificacion 		= models.ForeignKey('Edificacion')

    #Representa el numero del informe 1 - 6.
    informe 		    = models.PositiveIntegerField(null=True, blank=True) 
    #Representa la fecha de elaborcion del informe.
    fecha_elaboracion   = models.DateTimeField(auto_now_add = True) 

    #Nombre de la Iglesia (No creo que entre)
    #Miembros Actuales (Bautizados)	
    miembros_actuales   = models.PositiveIntegerField('Miembros Actuales', help_text='Bautizados')
    #Total miembros nuevos
    nuevos_miembros     = models.PositiveIntegerField('Total Miembros Nuevos', help_text='Total de miembros agregados a la membresía de la iglesia en los últimos 6 meses')

    conversiones        = models.PositiveIntegerField('Conversiones', help_text='Total de personas que aceptaron a Cristo como su Señor y Salvador en el último semestre')
 
    bautismos_nuevos    = models.PositiveIntegerField('Total Bautismos')
    no_bautismos        = models.TextField('Si no hubo bautismos', help_text='Explique por que no hubo bautismos', null=True, blank=True)
    #Total Asistencia general incluyendo niños y no bautizados
    asistencia_general  = models.PositiveIntegerField('Total Asistencia General', help_text='Servicios dominicales y grupos de vida incluyendo niños y no bautizados')
    #Numero de Grupos de vida o Celulas en Julio-Diciembre 2015
    grupos_vida         = models.PositiveIntegerField('Grupos de vida o Celulas', help_text='Número actual de grupos de vida, grupos evangelísticos, casas de oración, grupos pequeños en casas etc..')
    #Plantacion de Iglesias: Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas entre Julio-Diciembre 2015
    plantacion          = models.PositiveIntegerField('Plantacion de Iglesias', help_text='Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas en el último semestre')
    
    plantacion_nombre_1 = models.CharField('', max_length=30)
    plantacion_lugar_1  = models.CharField('', max_length=30)
    plantacion_fecha_1  = models.CharField('', max_length=30)

    plantacion_nombre_2 = models.CharField('', max_length=30)
    plantacion_lugar_2  = models.CharField('', max_length=30)
    plantacion_fecha_2  = models.CharField('', max_length=30)

    plantacion_nombre_3 = models.CharField('', max_length=30)
    plantacion_lugar_3  = models.CharField('', max_length=30)
    plantacion_fecha_3  = models.CharField('', max_length=30)

    asistencia_grupos   = models.PositiveIntegerField('Asistencia grupos de vida', help_text='Asistencia promedio (por grupo no general) a los grupos de vida')

    ofrendas            = models.PositiveIntegerField('Ofrendas y Diezmos', help_text='Total dinero recaudado en ofrendas y diezmos en el último semestre')
    #Peticiones de oracion especificas, accion de gracias o preocupaciones
    peticiones_oracion  = models.TextField('Peticiones de Oracion', 
                        help_text='Especificas, accion de gracias o preocupaciones, favor explicar o dar detalles de la petición')
    #Testimonios (liberaciones, conversiones, milagros, etc)
    testimonios  		= models.TextField('Testimonios', 
                        help_text='liberaciones, conversiones, milagros, etc. Favor relatar brevemente el testimonio detallando quien como y donde')
    #Ministerio de los niños (campamentos. alcances evangelisticos, escuela biblica, deportes,grupos de vida, etc.)
    ministerio_ninos  	= models.TextField('Ministerio de los Niños', 
                        help_text='Describa las últimas actividades con niños en el último semestre como: campamentos, alcances evangelisticos, escuela bíblica, deportes,grupos de vida, etc.')
    #Uso del local de la iglesia (Escuela de dia, entrenamiento vocacional, estudios biblicos, ministerio femenino, proyeccion de peliculas, etc.)
    uso_local		  	= models.TextField('Uso del local de la iglesia', 
                        help_text='Como se uso el local en el último semestre. ej.: Escuela de día, entrenamiento vocacional, estudios bíblicos, ministerio de mujeres, proyección de películas etc.')
    
    fotos               = models.FileField('Fotos evidencia', upload_to=ruta_fotos_informe_semestral, validators=[validate_comprimidos], help_text='Suba un un archivo comprimido en .rar o .zip de fotos que evidencien los programas realizados en el templo' )

    #Para mayor información o inquietudes comuníquese a:
    #	Victor Rincon
    #	Asistente Nacional
    #	(300) 8952603

    def __str__(self):
        return "%s" %"Informe Semestral"


def ruta_fotos_informe_publico(self, filename):
	return 'informes/%s' %(filename)


class InformeSemestralPublico(models.Model):
    """ Este modelo es para eviar informes sin loguin """

    class Meta:
        verbose_name_plural = "informes públicos"

    REGION_CHOICES = (
		(0, 'Central'),
		(1, 'Sur Oriental'),
		(2, 'Mecusab'),
		(3, 'Pacífico'),
		(4, 'Sur'),
		(5, 'Valle'),
		(6, 'Guanbianos'),
		(7, 'Paez'),
        (8, 'Bautista')
	)
    
    nombre_proyecto     = models.CharField('Nombre', max_length=40)
    persona             = models.CharField('Encargado', max_length=40)
    email               = models.EmailField(max_length=255)
    telefono            = models.CharField('Teléfono', max_length=40, help_text='Celular y/o teléfono, puede poner ambos separados por coma')
    depto 				= models.CharField('Departamento', max_length=30, choices=DEPTOS)
    municipio           = models.CharField(max_length=30)
    direccion 		    = models.TextField('Dirección')
    region 				= models.SmallIntegerField('Región', choices=REGION_CHOICES, help_text='La Región a la que pertenece la Iglesia')


    miembros_actuales   = models.PositiveIntegerField('Miembros Actuales', help_text='Bautizados')

    nuevos_miembros     = models.PositiveIntegerField('Total Miembros Nuevos', help_text='Total de miembros agregados a la membresía de la iglesia en los últimos 6 meses')

    conversiones        = models.PositiveIntegerField('Conversiones', help_text='Total de personas que aceptaron a Cristo como su Señor y Salvador en el último semestre')
 
    bautismos_nuevos    = models.PositiveIntegerField('Total Bautismos', help_text="Total de personas bautizadas en el último semestre")
    no_bautismos        = models.TextField('Si no hubo bautismos', help_text='Explique por que no hubo bautismos', null=True, blank=True)
 
    asistencia_general  = models.PositiveIntegerField('Total Asistencia General', help_text='Servicios dominicales y grupos de vida incluyendo niños y no bautizados')

    grupos_vida         = models.PositiveIntegerField('Grupos de vida o Células', help_text='Número actual de grupos de vida, grupos evangelísticos, casas de oración, grupos pequeños en casas etc..')

    plantacion_nombre_1 = models.CharField('', max_length=30)
    plantacion_lugar_1  = models.CharField('', max_length=30)
    plantacion_fecha_1  = models.CharField('', max_length=30)

    plantacion_nombre_2 = models.CharField('', max_length=30)
    plantacion_lugar_2  = models.CharField('', max_length=30)
    plantacion_fecha_2  = models.CharField('', max_length=30)

    plantacion_nombre_3 = models.CharField('', max_length=30)
    plantacion_lugar_3  = models.CharField('', max_length=30)
    plantacion_fecha_3  = models.CharField('', max_length=30)

    asistencia_grupos   = models.PositiveIntegerField('Asistencia grupos de vida', help_text='Asistencia promedio (por grupo no general) a los grupos de vida')

    ofrendas            = models.PositiveIntegerField('Ofrendas y Diezmos', help_text='Total dinero recaudado en ofrendas y diezmos en el último semestre')

    peticiones_oracion  = models.TextField('Peticiones de Oracion', 
                        help_text='Especificas, accion de gracias o preocupaciones, favor explicar o dar detalles de la petición')

    testimonios  		= models.TextField('Testimonios', 
                        help_text='liberaciones, conversiones, milagros, etc. Favor relatar brevemente el testimonio detallando quien como y donde')

    ministerio_ninos  	= models.TextField('Ministerio de los Niños', 
                        help_text='Describa las últimas actividades con niños en el último semestre como: campamentos, alcances evangelisticos, escuela bíblica, deportes,grupos de vida, etc.')

    uso_local		  	= models.TextField('Uso del local de la iglesia', 
                        help_text='Como se uso el local en el último semestre. ej.: Escuela de día, entrenamiento vocacional, estudios bíblicos, ministerio de mujeres, proyección de películas etc.')
    
    fotos               = models.FileField('Fotos evidencia', upload_to=ruta_fotos_informe_publico, validators=[validate_comprimidos], help_text='Suba un un archivo comprimido en .rar o .zip de fotos que evidencien los programas realizados en el templo' )


    created     = models.DateTimeField(auto_now_add = True) 
    updated     = models.DateField(auto_now = True) 

    def get_absolute_url(self):
		return reverse('main.views.informe_semestral', args=[str(self.id)])
    

    def __unicode__(self):
		return "%s %s" %(self.id, u"Informe Público")

