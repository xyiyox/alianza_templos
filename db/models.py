# -*- coding: utf-8 -*-
from django.db import models
from .datos import *
from map_field import fields as map_fields
from django.conf import settings


class Edificacion(models.Model):
	"""
	Representacion de un Proyecto de construccion 
	de un templo para una iglesia de la IACYMC
	"""

	class Meta:
		verbose_name_plural = "edificaciones"
			
	nombre_proyecto = models.CharField(max_length=40, verbose_name='Nombre del Proyecto')
	direccion = models.TextField(verbose_name='Dirección')
	coordenadas = map_fields.GeoLocationField(max_length=100, help_text=EDIFICACION_COORDENADAS) 

	TIPO_OWNER_LOTE_CHOICES = (
		(0, 'Alianza Cristiana'),
		(1, 'Otro'),
	)
	owner_lote= models.SmallIntegerField('Dueño del Lote', choices=TIPO_OWNER_LOTE_CHOICES)

	TIPO_ADQUISICION_CHOICES = (
		(0, 'Comprado'),
		(1, 'Donado'),
	)
	tipo_adquisicion = models.SmallIntegerField('Método de Adquisición', choices=TIPO_ADQUISICION_CHOICES)

	dimensiones_terreno = models.CharField('Dimensiones del Terreno', max_length=30, help_text=
		"Ingrese Ancho x Largo en Metros")

	dimensiones_edificio = models.CharField('Dimensiones del Edificio',max_length=30, help_text=
		"Ingrese las medidas en Metros")

	num_pisos = models.SmallIntegerField('Cantidad de Pisos', choices=((0, 1), (1, 2)), default=0 )

	TIPO_CONSTRUCCION_CHOICES = (
		(0, 'Iglesia',),
		(1, 'Guarderia'),
		(2, 'Iglesia/Guarderia'),
	)
	tipo_construccion = models.SmallIntegerField('Tipo de Construcción', choices=TIPO_CONSTRUCCION_CHOICES)

	METODO_CONSTRUCCION_CHOICES = (
		(0, 'Nueva Edificacion'),
		(1, 'Otro'),
	)
	metodo_construccion = models.SmallIntegerField('Método de Construcción',choices=METODO_CONSTRUCCION_CHOICES)

	requiere_permiso = models.BooleanField('¿Requiere de un permiso de construcción?')

	tiempo_limite = models.PositiveSmallIntegerField('Tiempo Limite', help_text='Tiempo en que se terminará la construcción (Meses)')

	#foto_construccion = models.ImageField('Foto del sitio de la construcción', upload_to='media')

	ESTADO_FORMULARIO = (
		(0, 'EdificacionForm'),
		(1, 'ComunidadForm'),
		(2, 'CongregacionForm'),
		(3, 'FuentesFinancierasForm'),
		(4, 'CondicionesForm'),
		(5, 'Terminado'),
	)
	estado = models.SmallIntegerField(choices=ESTADO_FORMULARIO)

	ETAPA_ACTUAL = (
		(0, 'En Diligenciamiento'),
		(1, 'En Revisión Regional'), # 1 semana para revisar por usuario regional
		(2, 'Aprobado por la Regional'),
		(3, 'En Revisión Nacional'), # 1 semana para revisar por usuario nacional
		(4, 'Esperando Cupo'),
		(5, 'Esperando Fondos'),
		(6, 'En Construcción'),
		(7, 'Finalizado'),
		(8, 'Esperando Correcciones'),
		(9, 'Rechazado'),
	)
	etapa_actual = models.PositiveSmallIntegerField(choices=ETAPA_ACTUAL)

	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Responsable')

	def __str__(self):
		return "%s" %"Edificación"


class InformacionFinanciera(models.Model):
	""" Informacion Financiera """

	class Meta:
		verbose_name_plural = "informaciones financieras"

	# Contribuciones estimadas de la congregacion
	mano_obra 			= models.PositiveIntegerField('Costo de la Mano de obra', default=0, blank=True)
	valor_materiales 	= models.PositiveIntegerField('Costo de Materiales de construcción', default=0, blank=True)
	dinero_efectivo 	= models.PositiveIntegerField('Dinero Ahorrado', 
							help_text='Ingrese el valor en Dolares (Estados Unidos). <br>Puede usar '
							'<a href="http://www.colombia.com/cambio_moneda/" target="_blank">este enlace</a> '
							'como convertidor de moneda.')
	valor_terreno 		= models.PositiveIntegerField('Valor del Terreno', 
							help_text='Ingrese el valor en Dolares (Estados Unidos)')
	VALOR_SOLICITADO_CHOICES = (
		(0, 14000),
		(1, 25000),
		(2, 39000),
	)
	valor_solicitado 	= models.PositiveIntegerField('Dinero solicitado', choices= VALOR_SOLICITADO_CHOICES, 
							help_text='Recuerde que este dinero esta expresado en Dolares (Estados Unidos)')
	costo_total 		= models.PositiveIntegerField('Costo total del proyecto', 
							help_text='Ingrese el valor en Dolares (Estados Unidos)')
	TIPO_PAGO_FONDO = (
		(0, 'Cuota Fija Mensual'),
		(1, 'Porcentaje Mensual de Ofrendas'),
	)

	edificacion 		= models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la informacion financiera

	def __str__(self):
		return "%s" %"Información Financiera"

class Comunidad(models.Model):
	""" Informacion de la ciudad """

	class Meta:
		verbose_name_plural = "ciudades"

	nombre 				= models.CharField('Nombre', max_length=50)
	poblacion_comunidad = models.CharField('Cantidad de población', max_length=40)
	region 				= models.CharField('Departamento', max_length=30) 
	
	capital_depto 		= models.CharField('Capital del Departamento', max_length=30)
	distancia_capital	= models.PositiveSmallIntegerField('Distancia a la capital', 
							help_text="Por favor ingrese el valor en Kilometros (Km)")

	edificacion 		= models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la comunidad

	def __str__(self):
		return "%s" %"Ciudad"

class Congregacion(models.Model):
	""" Informacion de la congregación """

	class Meta:
		verbose_name_plural = "congregaciones"

	nombre 				= models.CharField(max_length=30)
	fecha_fundacion 	= models.DateField('Fecha de Fundación', help_text='Dia/Mes/Año')
	lengua_primaria 	= models.CharField('Lengua primaria hablada', max_length=20)
	REGION_CHOICES = (
		(0, 'Central'),
		(1, 'Sur Oriental'),
		(2, 'Mecusab'),
		(3, 'Pacífico'),
		(4, 'Sur'),
		(5, 'Valle'),
	)
	region 					= models.SmallIntegerField('Región', choices=REGION_CHOICES, 
							help_text='La Región a la que pertenece la Iglesia')
	asistencia_general 		= models.SmallIntegerField('Asistencia general promedio')
	asistencia_ninos 		= models.SmallIntegerField('Asistencia general promedio de niños')
	miembros_adultos 		= models.SmallIntegerField('Cantidad de miembros adultos', 
							help_text='Recuerde que se considera como miembro a aquel que ha sido bautizado')
	miembros_ninos 			= models.SmallIntegerField('Cantidad de miembros niños')
	ingreso_mensual 		= models.DecimalField('Ingreso mensual promedio', max_digits=15, decimal_places=3)

	""" 
	Informacion del Pastor 
	"""
	nombre_pastor 			= models.CharField('Nombre del pastor', max_length=50)
	ESTADO_CIVIL_CHOICES = (
		(0, 'Soltero'),
		(1, 'Casado'),
		(2, 'Viudo'),
		(3, 'Otro'),
	)
	estado_civil 			= models.SmallIntegerField('Estado civil', choices=ESTADO_CIVIL_CHOICES)
	cant_hijos 				= models.PositiveSmallIntegerField('Cantidad de hijos')
	entrenamiento_biblico 	= models.PositiveSmallIntegerField('Años de entrenamiento Biblico')
	titulos_obtenidos 		= models.CharField('Titulos obtenidos', max_length=70)
	anios_iglesia 			= models.PositiveSmallIntegerField('Años de servicio en la congregación actual')
	anios_ministerio 		= models.PositiveSmallIntegerField('Años de servicio en el ministerio')

	hay_material 			= models.BooleanField('¿El pastor conoce el material del Instituto Biblico del Aire?')
	q1_why_not 				= models.TextField('¿Por que no?', blank=True, null=True)
	usa_material			= models.BooleanField('¿El pastor ha acordado usar este material para crecimiento de la iglesia?') 
	q2_why_not 				= models.TextField('¿Por que no?', blank=True, null=True)
	q2_how_do 				= models.TextField('¿Como lo hace?', blank=True, null=True)
	
	edificacion 			= models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la congregacion

	def __str__(self):
		return "%s" %"Congregación"
	
class Fuentes_Financiacion(models.Model):
	""" 
	Tabla que almacenara posibles entradas economicas dinstintas a ICM que tenga el proyecto
	"""
	nombre 			= models.CharField(max_length=30)
	valor 			= models.DecimalField('Valor', max_digits=15, decimal_places=3)
	
	info_financiera = models.ForeignKey('InformacionFinanciera')


class Condiciones(models.Model):
	""" Condiciones """

	class Meta:
		verbose_name_plural = "condiciones"

	edificacion       = models.ForeignKey('Edificacion')
	construccion      = models.BooleanField(CONDICIONES_CONSTRUCCION, choices=BOOL_CHOICES)
	mantenimiento     = models.BooleanField(CONDICIONES_MANTENIMIENTO, choices=BOOL_CHOICES)
	actividades       = models.BooleanField(CONDICIONES_ACTIVIDADES, choices=BOOL_CHOICES)
	discipulado       = models.BooleanField(CONDICIONES_DISCIPULADO, choices=BOOL_CHOICES)
	alcance           = models.BooleanField(CONDICIONES_ALCANCE, choices=BOOL_CHOICES)
	
	found_trust       = models.BooleanField(CONDICIONES_FOUND_TRUST, choices=BOOL_CHOICES)
	found_commitment  = models.BooleanField(CONDICIONES_FOUND_COMMITMENT, choices=BOOL_CHOICES)
	found_payment     = models.CharField(CONDICIONES_FOUND_PAYMENT, max_length=20, help_text='Cantidad o Porcentaje')

	presupuesto       = models.BooleanField(CONDICIONES_PRESUPUESTO, choices=BOOL_CHOICES)
	terminacion       = models.BooleanField(CONDICIONES_TERMINACION, choices=BOOL_CHOICES)
	comentarios       = models.TextField(CONDICIONES_COMENTARIOS, blank=True)
	aceptacion        = models.BooleanField(help_text=CONDICIONES_ACEPTACION)
	nombre_completo   = models.CharField(max_length=50, help_text=CONDICIONES_FULL_NAME)

	def __str__(self):
		return "%s" %"Condiciones"


class Adjuntos(models.Model):
	""" Modelo para almacenar los archivos adjuntos """

	class Meta:
		verbose_name_plural = "adjuntos"

	edificacion   			= models.ForeignKey('Edificacion')

	foto_construccion 		= models.ImageField('Foto del sitio de construcción', upload_to='adjuntos',
								help_text='Mostrando claramente el área donde se va a construir la iglesia')
	foto_congregacion 		= models.ImageField('Foto de la congregación', upload_to='adjuntos', 
								help_text='Mostrando el lugar donde se reunen actualmente')
	foto_pastor 			= models.FileField('Foto del Pastor', upload_to='adjuntos', null=True, blank=True,
								help_text='Incluya una foto del pastor en caso de no aparecer en la foto de la congregación')

	permiso_construccion 	= models.FileField('Permiso de construcción', upload_to='adjuntos', null=True, blank=True,
								help_text='Si se requiere, debe agregarlo')
	escritura_terreno 		= models.FileField('Escritura del terreno', upload_to='adjuntos',
								help_text='Mostrando la prueba de propiedad')
	plan_terreno 			= models.FileField('Plan de Terreno', upload_to='adjuntos', 
								help_text='Mostrando las dimensiones de la propiedad y la ubicación de la tierra')
	plan_construccion 		= models.FileField('Plan de construcción', upload_to='adjuntos', null=True, blank=True,
								help_text='Obligatorio para todos los planes que no hacen parte de los aprobados por ICM')
	historia_congregacion 	= models.FileField('Historia de la congregación', upload_to='adjuntos',
								help_text='Incluya una breve historia de la congregación')
	testimonio_pastor 		= models.FileField('Testimonio del pastor', upload_to='adjuntos',
								help_text='Incluya el testimonio del pastor de la congregación')	

	def __str__(self):
		return "%s" %"Adjuntos"

class Comentario(models.Model):
	""" Modelo para almacenar los comentarios de una edificacion """
	
	edificacion = models.ForeignKey('Edificacion')
	commenter 	= models.ForeignKey(settings.AUTH_USER_MODEL)
	descripcion = models.TextField('Comentario')