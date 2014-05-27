# -*- coding: utf-8 -*-
from django.db import models
from djgeojson.fields import PointField
from .datos import *


class Edificacion(models.Model):
	"""
	Representacion de un Proyecto de construccion 
	de un templo para una iglesia de la IACYMC
	"""
	nombre_proyecto = models.CharField(max_length=40, verbose_name='Nombre del Proyecto')
	direccion = models.TextField(verbose_name='Dirección')
	coordenadas = PointField()
	TIPO_OWNER_ESCRITURA_CHOICES = (
		(0, 'Partner Organization'),
		(1, 'Congregacion'),
		(2, 'Lideres de la Iglesia'),
		(3, 'Otro'),
	)
	owner_escritura = models.SmallIntegerField('Dueño de la escritura', choices=TIPO_OWNER_ESCRITURA_CHOICES)
	TIPO_ADQUISICION_CHOICES = (
		(0, 'Comprado'),
		(1, 'Donado'),
	)
	tipo_adquisicion = models.SmallIntegerField('Método de Adquisición', choices=TIPO_ADQUISICION_CHOICES)

	tiempo_limite = models.PositiveSmallIntegerField('Tiempo Limite', help_text='en que se terminará la construcción (Meses)')
	dimensiones_terreno = models.CharField('Dimensiones del Terreno', max_length=30)
	dimensiones_edificio = models.CharField('Dimensiones del Edificio',max_length=30)
	TIPO_CONSTRUCCION_CHOICES = (
		(0, 'Iglesia'),
		(1, 'Capilla'),
		(2, 'Otro'),
	)
	tipo_construccion = models.SmallIntegerField('Tipo de Construcción', choices=TIPO_CONSTRUCCION_CHOICES)
	METODO_CONSTRUCCION_CHOICES = (
		(0, 'Nueva Edificacion'),
		(1, 'Otro'),
	)
	metodo_construccion = models.SmallIntegerField('Método de Construcción',choices=METODO_CONSTRUCCION_CHOICES)

	requiere_permiso = models.BooleanField('¿Requiere de un permiso de construcción?')
	is_icm_approved = models.BooleanField('¿Ya ha sido aprobado por la ICM?')
	moneda_local = models.CharField('Moneda Local',max_length=20)

	""" Informacion Financiera """
	# Contribuciones estimadas de la congregacion
	mano_obra = models.DecimalField('Mano de obra', max_digits=12, decimal_places=3)
	valor_materiales = models.DecimalField('Materiales de construcción', max_digits=15, decimal_places=3)
	dinero_efectivo = models.DecimalField('Dinero en efectivo', max_digits=15, decimal_places=3)
	aporte_terreno = models.DecimalField('Aporte para el Terreno', max_digits=12, decimal_places=3)

	valor_solicitado = models.DecimalField('Dinero solicitado', max_digits=12, decimal_places=3)
	costo_total = models.DecimalField('Costo total del proyecto', max_digits=12, decimal_places=3)

	TIPO_PAGO_FONDO = (
		(0, 'Cuota Fija Mensual'),
		(1, 'Porcentaje Mensual de Ofrendas'),
	)
	pago_fondo = models.SmallIntegerField('¿Como se pagara el fondo?',choices=TIPO_PAGO_FONDO)

	ESTADO_FORMULARIO = (
		(0, 'EdificacionForm'),
		(1, 'ComunidadForm'),
		(2, 'CongregacionForm'),
		(3, 'FuentesFinancierasForm'),
		(4, 'CondicionesForm'),
		(5, 'Terminado'),
	)
	estado = models.SmallIntegerField()

class Comunidad(models.Model):
	""" Informacion de la comunidad """
	poblacion_comunidad = models.CharField(max_length=40)
	nombre = models.CharField('Nombre', max_length=50)
	region = models.CharField('Region, Estado o Distrito', max_length=30) # Tambien puede ser estado, region o distrito
	pais = models.CharField('Pais', max_length=20)
	
	ciudad_cercana = models.CharField('Nombre de la ciudad mas cercana', max_length=30)
	distancia_ciudad= models.PositiveSmallIntegerField('Distancia a la ciudad mas cercana (Km)') # En km
	iglesia_cercana = models.CharField('Nombre de la iglesia mas cercana', max_length=30)
	distancia_iglesia = models.PositiveSmallIntegerField('Distancia a la iglesia mas cercana (Km)') # En km

	edificacion = models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la comunidad

class Congregacion(models.Model):
	nombre = models.CharField(max_length=30)
	lengua_primaria = models.CharField('Lengua primaria hablada', max_length=20)
	fecha_fundacion = models.DateField('Fecha de fundación')
	asistentes_adultos = models.SmallIntegerField('Promedio de adultos por servicio')
	asistentes_ninos = models.SmallIntegerField('Promedio de niños por servicio')
	miembros_adultos = models.SmallIntegerField('Cantidad de miembros adultos')
	miembros_ninos = models.SmallIntegerField('Cantidad de miembros niños')

	ingresos_ofrendas = models.DecimalField('Ingresos por ofrendas', max_digits=15, decimal_places=3) # ¿Unidad del dinero? Mensual

	nombre_pastor = models.CharField('Nombre del pastor', max_length=50)
	entrenamiento_biblico = models.CharField('Entrenamiento Biblico', max_length=50)
	ESTADO_CIVIL_CHOICES = (
		(0, 'Soltero'),
		(1, 'Casado'),
	)
	estado_civil = models.SmallIntegerField('Estado civil', choices=ESTADO_CIVIL_CHOICES)
	numero_hijos = models.PositiveSmallIntegerField('Número de hijos')
	titulos_obtenidos = models.CharField('Titulos obtenidos', max_length=50)
	anios_iglesia = models.PositiveSmallIntegerField('Años de servicio en la congregación')
	anios_ministerio = models.PositiveSmallIntegerField('Años de servicio en el ministerio')
	# Se debe almacenar una foto del pastor

	hay_material = models.BooleanField('¿El pastor ha hablado de la disponibilidad de material para estudio biblico?')
	q1_why_not = models.TextField('¿Por que no?', blank=True, null=True)
	usa_material = models.BooleanField('¿El pastor ha acordado usar este material para crecimiento de la iglesia?') 
	q2_why_not = models.TextField('¿Por que no?', blank=True, null=True)
	q2_how_do = models.TextField('¿Como lo hace?', blank=True, null=True)
	
	edificacion = models.OneToOneField('Edificacion') # Relacion 1 a 1 entre la edificacion y la congregacion
	
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

class Adjuntos(models.Model):
	""" Modelo para almacenar los archivos adjuntos """
	# edificacion   = models.ForeignKey('Edificacion')
	TIPO_ARCHIVO_CHOICES = (
		(0, 'Foto del Sitio de Construccion'),
		(1, 'Foto de la Congregacion'),
		(2, 'Foto del Pastor'),
		(3, 'Copia del Permiso de Construccion'),
		(4, 'Copia de la Escritura de Propiedad'),
		(5, 'Copy of the Plot Plan '),
		(6, 'Copia del Plan de Construccion'),
		(7, 'Breve Historia de la Congregacion'),
		(8, 'Testimonio del Pastor'),
	)
	tipo_archivo  = models.SmallIntegerField(choices=TIPO_ARCHIVO_CHOICES)
	archivo_adjunto = models.FileField(upload_to='media')
	
