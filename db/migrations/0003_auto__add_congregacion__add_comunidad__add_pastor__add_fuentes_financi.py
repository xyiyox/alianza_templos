# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Congregacion'
        db.create_table(u'db_congregacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lengua_primaria', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fecha_fundacion', self.gf('django.db.models.fields.DateField')()),
            ('asistentes_adultos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('asistentes_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('miembros_adultos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('miembros_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('ingresos_ofrendas', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('q1_hay_material_biblico', self.gf('django.db.models.fields.BooleanField')()),
            ('q1_why_not', self.gf('django.db.models.fields.TextField')()),
            ('q2_usa_material', self.gf('django.db.models.fields.BooleanField')()),
            ('q2_why_not', self.gf('django.db.models.fields.TextField')()),
            ('q2_how_do', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'db', ['Congregacion'])

        # Adding model 'Comunidad'
        db.create_table(u'db_comunidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poblacion_comunidad', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ciudad_cercana', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('distancia_ciudad', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('iglesia_cercana', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('distancia_iglesia', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'db', ['Comunidad'])

        # Adding model 'Pastor'
        db.create_table(u'db_pastor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('entrenamiento_biblico', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado_civil', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('numero_hijos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('titulos_obtenidos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('anios_iglesia', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('anios_ministerio', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'db', ['Pastor'])

        # Adding model 'Fuentes_Financieras'
        db.create_table(u'db_fuentes_financieras', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('valor_local', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('valor_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
        ))
        db.send_create_signal(u'db', ['Fuentes_Financieras'])


    def backwards(self, orm):
        # Deleting model 'Congregacion'
        db.delete_table(u'db_congregacion')

        # Deleting model 'Comunidad'
        db.delete_table(u'db_comunidad')

        # Deleting model 'Pastor'
        db.delete_table(u'db_pastor')

        # Deleting model 'Fuentes_Financieras'
        db.delete_table(u'db_fuentes_financieras')


    models = {
        u'db.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'ciudad_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'distancia_ciudad': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'distancia_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iglesia_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'poblacion_comunidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'db.congregacion': {
            'Meta': {'object_name': 'Congregacion'},
            'asistentes_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'asistentes_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fecha_fundacion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos_ofrendas': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'lengua_primaria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'miembros_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'miembros_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'q1_hay_material_biblico': ('django.db.models.fields.BooleanField', [], {}),
            'q1_why_not': ('django.db.models.fields.TextField', [], {}),
            'q2_how_do': ('django.db.models.fields.TextField', [], {}),
            'q2_usa_material': ('django.db.models.fields.BooleanField', [], {}),
            'q2_why_not': ('django.db.models.fields.TextField', [], {})
        },
        u'db.fuentes_financieras': {
            'Meta': {'object_name': 'Fuentes_Financieras'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valor_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'valor_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'})
        },
        u'db.pastor': {
            'Meta': {'object_name': 'Pastor'},
            'anios_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'anios_ministerio': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'entrenamiento_biblico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estado_civil': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero_hijos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'titulos_obtenidos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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