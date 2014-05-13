# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Proyecto.latitud'
        db.delete_column(u'db_proyecto', 'latitud')

        # Deleting field 'Proyecto.longitud'
        db.delete_column(u'db_proyecto', 'longitud')

        # Adding field 'Proyecto.coordenadas'
        db.add_column(u'db_proyecto', 'coordenadas',
                      self.gf('djgeojson.fields.PointField')(default='{}'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Proyecto.latitud'
        raise RuntimeError("Cannot reverse this migration. 'Proyecto.latitud' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Proyecto.latitud'
        db.add_column(u'db_proyecto', 'latitud',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=4),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Proyecto.longitud'
        raise RuntimeError("Cannot reverse this migration. 'Proyecto.longitud' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Proyecto.longitud'
        db.add_column(u'db_proyecto', 'longitud',
                      self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=4),
                      keep_default=False)

        # Deleting field 'Proyecto.coordenadas'
        db.delete_column(u'db_proyecto', 'coordenadas')


    models = {
        u'db.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'anios_en_actual_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'anios_en_ministerio': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'aporte_fuente1_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'aporte_fuente1_monedalocal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'aporte_fuente2_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'aporte_fuente2_monedalocal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'aporte_solicitado_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'aporte_solicitado_monedalocal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'cant_asistentes_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cant_asistentes_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cant_miembros_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cant_miembtos_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cantidad_hijos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'ciudad_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'coordenadas': ('djgeojson.fields.PointField', [], {}),
            'coste_total_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'coste_total_monedalocal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'dimensiones_edificio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_terreno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dinero_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'dinero_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'distancia_ciudad_cercana': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'distancia_iglesia_cercana': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'dolar_en_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'entrenamiento_biblico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estado_civil': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fecha_fundacion': ('django.db.models.fields.DateField', [], {}),
            'fuente1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fuente2': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iglesia_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ingresos_ofrendas': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'is_icm_approved': ('django.db.models.fields.BooleanField', [], {}),
            'labor_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'labor_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'lengua_primaria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'materiales_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'materiales_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'metodo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'moneda_local': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nombre_comunidad': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_pastor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner_escritura': ('django.db.models.fields.SmallIntegerField', [], {}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'poblacion_comunidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'q1_disponibilidad_material_estudio_biblico': ('django.db.models.fields.BooleanField', [], {}),
            'q1_why_not': ('django.db.models.fields.TextField', [], {}),
            'q2_how_do': ('django.db.models.fields.TextField', [], {}),
            'q2_usa_material_crecimiento_iglesia': ('django.db.models.fields.BooleanField', [], {}),
            'q2_why_not': ('django.db.models.fields.TextField', [], {}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'requiere_permiso_construccion': ('django.db.models.fields.BooleanField', [], {}),
            'terreno_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'terreno_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'tiempo_terminar_construccion': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tipo_adquisicion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tipo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'titulos_obtenidos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['db']