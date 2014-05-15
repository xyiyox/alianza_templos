# -*- coding: utf-8 -*-
from django.db import models
from djgeojson.fields import PointField
from .datos import *


class Edificacion(models.Model):
	"""
	Representacion de un Proyecto de construccion 
	de un templo para una iglesia de la IACYMC
	"""
	nombre_proyecto = models.CharField(max_length=40)
	direccion = models.TextField()
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
	tipo_adquisicion = models.SmallIntegerField()

	tiempo_limite = models.PositiveSmallIntegerField()
	dimensiones_terreno = models.CharField(max_length=30)
	dimensiones_edificio = models.CharField(max_length=30)
	TIPO_CONSTRUCCION_CHOICES = (
		(0, 'Iglesia'),
		(1, 'Capilla'),
		(2, 'Otro'),
	)
	tipo_construccion = models.SmallIntegerField()
	METODO_CONSTRUCCION_CHOICES = (
		(0, 'Nueva Edificacion'),
		(1, 'Otro'),
	)
	metodo_construccion = models.SmallIntegerField()
	congregacion = models.OneToOneField('Congregacion') # Relacion 1 a 1 entre la edificacion y la congregacion

	requiere_permiso = models.BooleanField()
	is_icm_approved = models.BooleanField()
	moneda_local = models.CharField(max_length=20)
	dolar_moneda_local = models.DecimalField(max_digits=6, decimal_places=3)

	""" Informacion Financiera """
	# Contribuciones estimadas de la congregacion
	labor_moneda_local = models.DecimalField(max_digits=12, decimal_places=3)
	labor_dolares = models.DecimalField(max_digits=12, decimal_places=3)
	materiales_moneda_local = models.DecimalField(max_digits=15, decimal_places=3)
	materiales_dolares = models.DecimalField(max_digits=15, decimal_places=3)
	dinero_moneda_local = models.DecimalField(max_digits=15, decimal_places=3)
	dinero_dolares = models.DecimalField(max_digits=15, decimal_places=3)
	terreno_moneda_local = models.DecimalField(max_digits=12, decimal_places=3)
	terreno_dolares = models.DecimalField(max_digits=12, decimal_places=3)

	valor_solicitado_monedalocal = models.DecimalField(max_digits=12, decimal_places=3)
	valor_solicitado_dolares = models.DecimalField(max_digits=12, decimal_places=3)
	costo_total_monedalocal = models.DecimalField(max_digits=12, decimal_places=3)
	costo_total_dolares = models.DecimalField(max_digits=12, decimal_places=3)
	TIPO_PAGO_FONDO = (
		(0, 'Cuota Fija Mensual'),
		(1, 'Porcentaje Mensual de Ofrendas'),
	)
	pago_fondo = models.SmallIntegerField()

class Comunidad(models.Model):
	""" Informacion de la comunidad """
	poblacion_comunidad = models.CharField(max_length=40)
	nombre = models.CharField(max_length=50)
	region = models.CharField(max_length=30) # Tambien puede ser estado, region o distrito
	pais = models.CharField(max_length=20)
	
	ciudad_cercana = models.CharField(max_length=30)
	distancia_ciudad= models.PositiveSmallIntegerField() # En km
	iglesia_cercana = models.CharField(max_length=30)
	distancia_iglesia = models.PositiveSmallIntegerField() # En km

class Congregacion(models.Model):
	nombre = models.CharField(max_length=30)
	lengua_primaria = models.CharField(max_length=20)
	fecha_fundacion = models.DateField()
	asistentes_adultos = models.SmallIntegerField()
	asistentes_ninos = models.SmallIntegerField()
	miembros_adultos = models.SmallIntegerField()
	miembros_ninos = models.SmallIntegerField()

	ingresos_ofrendas = models.DecimalField(max_digits=15, decimal_places=3) # ¿Unidad del dinero? Mensual

	nombre_pastor = models.CharField(max_length=50)
	entrenamiento_biblico = models.CharField(max_length=50)
	ESTADO_CIVIL_CHOICES = (
		(0, 'Soltero'),
		(1, 'Casado'),
	)
	estado_civil = models.SmallIntegerField()
	numero_hijos = models.PositiveSmallIntegerField()
	titulos_obtenidos = models.CharField(max_length=50)
	anios_iglesia = models.PositiveSmallIntegerField()
	anios_ministerio = models.PositiveSmallIntegerField()
	# Se debe almacenar una foto del pastor

	q1_hay_material_biblico = models.BooleanField() # ¿El pastor ha hablado de la disponibilidad de material para estudio biblico?
	q1_why_not = models.TextField()
	q2_usa_material = models.BooleanField() # ¿El pastor ha acordado usar este material para crecimiento de la iglesia?
	q2_why_not = models.TextField()
	q2_how_do = models.TextField()
	
	
class Fuentes_Financieras(models.Model):
	""" 
	Tabla que almacenara entradas economicas como mano de obra, materiales
	"""
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	valor_local = models.DecimalField(max_digits=15, decimal_places=3)
	valor_dolares = models.DecimalField(max_digits=15, decimal_places=3)
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
