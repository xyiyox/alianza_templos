# -*- coding: utf-8 -*-
from django.db import models
from djgeojson.fields import PointField
from .datos import *
from map_field import fields as map_fields


class Edificacion(models.Model):
	"""
	Representacion de un Proyecto de construccion 
	de un templo para una iglesia de la IACYMC
	"""
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
	estado = models.SmallIntegerField()

	def __str__(self):
		return "Edificación"

class InformacionFinanciera(models.Model):
	""" Informacion Financiera """
	# Contribuciones estimadas de la congregacion
	mano_obra = models.DecimalField('Costo de la Mano de obra', max_digits=12, decimal_places=3)
	valor_materiales = models.DecimalField('Costo de Materiales de construcción', max_digits=15, decimal_places=3)
	dinero_efectivo = models.DecimalField('Dinero Ahorrado', max_digits=15, decimal_places=3)
	valor_terreno = models.DecimalField('Valor del Terreno', max_digits=12, decimal_places=3)
	VALOR_SOLICITADO_CHOICES = (
		(0, 14000),
		(1, 25000),
		(2, 39000),
	)
	valor_solicitado = models.DecimalField('Dinero solicitado', max_digits=12, decimal_places=3, 
		choices= VALOR_SOLICITADO_CHOICES, default=0)
	costo_total = models.DecimalField('Costo total del proyecto', max_digits=12, decimal_places=3)
	TIPO_PAGO_FONDO = (
		(0, 'Cuota Fija Mensual'),
		(1, 'Porcentaje Mensual de Ofrendas'),
	)

	edificacion = models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la informacion financiera

	def __str__(self):
		return "Información Financiera"

class Comunidad(models.Model):
	""" Informacion de la comunidad """
	nombre = models.CharField('Nombre', max_length=50)
	poblacion_comunidad = models.CharField('Cantidad de población', max_length=40)
	region = models.CharField('Departamento', max_length=30) 
	
	capital_depto = models.CharField('Capital del Departamento', max_length=30)
	distancia_capital= models.PositiveSmallIntegerField('Distancia a la capital', 
		help_text="Por favor ingrese el valor en Kilometros (Km)")

	edificacion = models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la comunidad

	def __str__(self):
		return "Comunidad"

class Congregacion(models.Model):
	nombre = models.CharField(max_length=30)
	lengua_primaria = models.CharField('Lengua primaria hablada', max_length=20)
	fecha_fundacion = models.DateField('Fecha de Fundación', help_text='Dia/Mes/Año')
	REGION_CHOICES = (
		(0, 'Central'),
		(1, 'Sur Oriental'),
		(2, 'Mecusab'),
		(3, 'Pacífico'),
		(4, 'Sur'),
		(5, 'Valle'),
	)
	region = models.SmallIntegerField('Región', choices=REGION_CHOICES, 
		help_text='La Región a la que pertenece la Iglesia')
	asistencia_general = models.SmallIntegerField('Asistencia general promedio')
	asistencia_ninos = models.SmallIntegerField('Asistencia general promedio de niños')
	miembros_adultos = models.SmallIntegerField('Cantidad de miembros adultos', 
		help_text='Recuerde que se considera como miembro a aquel que ha sido bautizado')
	miembros_ninos = models.SmallIntegerField('Cantidad de miembros niños', 
		help_text='Recuerde que se considera como miembro a aquel que ha sido bautizado')
	ingreso_mensual = models.DecimalField('Ingreso mensual promedio', max_digits=15, decimal_places=3)

	""" 
	Informacion del Pastor 
	"""
	nombre_pastor = models.CharField('Nombre del pastor', max_length=50)
	ESTADO_CIVIL_CHOICES = (
		(0, 'Soltero'),
		(1, 'Casado'),
		(2, 'Viudo'),
		(3, 'Otro'),
	)
	estado_civil = models.SmallIntegerField('Estado civil', choices=ESTADO_CIVIL_CHOICES)
	cant_hijos = models.PositiveSmallIntegerField('Cantidad de hijos')
	entrenamiento_biblico = models.PositiveSmallIntegerField('Años de entrenamiento Biblico')
	titulos_obtenidos = models.CharField('Titulos obtenidos', max_length=70)
	anios_iglesia = models.PositiveSmallIntegerField('Años de servicio en la congregación actual')
	anios_ministerio = models.PositiveSmallIntegerField('Años de servicio en el ministerio')

	hay_material = models.BooleanField('¿El pastor ha hablado de la disponibilidad de material para estudio biblico?')
	q1_why_not = models.TextField('¿Por que no?', blank=True, null=True)
	usa_material = models.BooleanField('¿El pastor ha acordado usar este material para crecimiento de la iglesia?') 
	q2_why_not = models.TextField('¿Por que no?', blank=True, null=True)
	q2_how_do = models.TextField('¿Como lo hace?', blank=True, null=True)
	
	edificacion = models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la congregacion

	def __str__(self):
		return "Congregación"
	
class Fuentes_Financieras(models.Model):
	""" 
	Tabla que almacenara entradas economicas como mano de obra, materiales
	"""
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField('Descripción')
	valor = models.DecimalField('Valor en moneda local', max_digits=15, decimal_places=3)
	
	edificacion = models.ForeignKey('Edificacion') # Relacion 1 a n entre edificacion y fuentes_financieras


class Condiciones(models.Model):
	""" Condiciones """
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
		return "Condiciones"

class Adjuntos(models.Model):
	""" Modelo para almacenar los archivos adjuntos """
	edificacion   			= models.ForeignKey('Edificacion')

	foto_construccion 		= models.ImageField('Foto del sitio de construcción', upload_to='media',
								help_text='Mostrando claramente el área donde se va a construir la iglesia')
	foto_congregacion 		= models.ImageField('Foto de la congregación', upload_to='media', 
								help_text='Mostrando el lugar donde se reunen actualmente')
	foto_pastor 			= models.FileField('Foto del Pastor', upload_to='media',
								help_text='Incluya una foto del pastor en caso de no aparecer en la foto de la congregación')

	permiso_construccion 	= models.FileField('Permiso de construcción', upload_to='media',
								help_text='Si se requiere, debe agregarlo')
	escritura_terreno 		= models.FileField('Escritura del terreno', upload_to='media',
								help_text='Mostrando la prueba de propiedad')
	plan_terreno 			= models.FileField('Plan de Terreno', upload_to='media', 
								help_text='Mostrando las dimensiones de la propiedad y la ubicación de la tierra')
	plan_construccion 		= models.FileField('Plan de construcción', upload_to='media',
								help_text='Obligatorio para todos los planes que no hacen parte de los aprobados por ICM')
	historia_congregacion 	= models.FileField('Historia de la congregación', upload_to='media',
								help_text='Incluya una breve historia de la congregación')
	testimonio_pastor 		= models.FileField('Testimonio del pastor', upload_to='media',
								help_text='Incluya el testimonio del pastor de la congregación')	

	def __str__(self):
		return "Adjuntos"