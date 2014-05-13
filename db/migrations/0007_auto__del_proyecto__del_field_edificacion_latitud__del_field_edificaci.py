# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Proyecto'
        db.delete_table(u'db_proyecto')

        # Deleting field 'Edificacion.latitud'
        db.delete_column(u'db_edificacion', 'latitud')

        # Deleting field 'Edificacion.longitud'
        db.delete_column(u'db_edificacion', 'longitud')

        # Adding field 'Edificacion.coordenadas'
        db.add_column(u'db_edificacion', 'coordenadas',
                      self.gf('djgeojson.fields.PointField')(default='{}'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Proyecto'
        db.create_table(u'db_proyecto', (
            ('coste_total_monedalocal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('coordenadas', self.gf('djgeojson.fields.PointField')()),
            ('fecha_fundacion', self.gf('django.db.models.fields.DateField')()),
            ('aporte_solicitado_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('labor_moneda_local', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('distancia_ciudad_cercana', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('cant_miembros_adultos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('is_icm_approved', self.gf('django.db.models.fields.BooleanField')()),
            ('cant_miembtos_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('entrenamiento_biblico', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dimensiones_edificio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('titulos_obtenidos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('materiales_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('labor_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('owner_escritura', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('metodo_construccion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('estado_civil', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('dinero_moneda_local', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('tiempo_terminar_construccion', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('terreno_moneda_local', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('moneda_local', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('distancia_iglesia_cercana', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('lengua_primaria', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('aporte_fuente1_monedalocal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('dolar_en_moneda_local', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poblacion_comunidad', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('terreno_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('ciudad_cercana', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cant_asistentes_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('tipo_construccion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('nombre_pastor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('q1_disponibilidad_material_estudio_biblico', self.gf('django.db.models.fields.BooleanField')()),
            ('q1_why_not', self.gf('django.db.models.fields.TextField')()),
            ('anios_en_actual_iglesia', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('requiere_permiso_construccion', self.gf('django.db.models.fields.BooleanField')()),
            ('aporte_solicitado_monedalocal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('aporte_fuente2_monedalocal', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('coste_total_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('q2_why_not', self.gf('django.db.models.fields.TextField')()),
            ('fuente2', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tipo_adquisicion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('fuente1', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('aporte_fuente1_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('aporte_fuente2_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('q2_usa_material_crecimiento_iglesia', self.gf('django.db.models.fields.BooleanField')()),
            ('nombre_comunidad', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dimensiones_terreno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ingresos_ofrendas', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('q2_how_do', self.gf('django.db.models.fields.TextField')()),
            ('dinero_dolares', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('cantidad_hijos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('materiales_moneda_local', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('cant_asistentes_adultos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('iglesia_cercana', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('anios_en_ministerio', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'db', ['Proyecto'])

        # Adding field 'Edificacion.latitud'
        db.add_column(u'db_edificacion', 'latitud',
                      self.gf('django.db.models.fields.DecimalField')(default=(0, 1), max_digits=8, decimal_places=4),
                      keep_default=False)

        # Adding field 'Edificacion.longitud'
        db.add_column(u'db_edificacion', 'longitud',
                      self.gf('django.db.models.fields.DecimalField')(default=(0, 0), max_digits=8, decimal_places=4),
                      keep_default=False)

        # Deleting field 'Edificacion.coordenadas'
        db.delete_column(u'db_edificacion', 'coordenadas')


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
        u'db.condiciones': {
            'Meta': {'object_name': 'Condiciones'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'db.congregacion': {
            'Meta': {'object_name': 'Congregacion'},
            'anios_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'anios_ministerio': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'asistentes_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'asistentes_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'entrenamiento_biblico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estado_civil': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fecha_fundacion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos_ofrendas': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'lengua_primaria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'miembros_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'miembros_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre_pastor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero_hijos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'q1_hay_material_biblico': ('django.db.models.fields.BooleanField', [], {}),
            'q1_why_not': ('django.db.models.fields.TextField', [], {}),
            'q2_how_do': ('django.db.models.fields.TextField', [], {}),
            'q2_usa_material': ('django.db.models.fields.BooleanField', [], {}),
            'q2_why_not': ('django.db.models.fields.TextField', [], {}),
            'titulos_obtenidos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'db.edificacion': {
            'Meta': {'object_name': 'Edificacion'},
            'congregacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Congregacion']", 'unique': 'True'}),
            'coordenadas': ('djgeojson.fields.PointField', [], {}),
            'costo_total_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'costo_total_monedalocal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'dimensiones_edificio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_terreno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dinero_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'dinero_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'dolar_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_icm_approved': ('django.db.models.fields.BooleanField', [], {}),
            'labor_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'labor_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'materiales_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'materiales_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'metodo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'moneda_local': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'owner_escritura': ('django.db.models.fields.SmallIntegerField', [], {}),
            'pago_fondo': ('django.db.models.fields.SmallIntegerField', [], {}),
            'requiere_permiso': ('django.db.models.fields.BooleanField', [], {}),
            'terreno_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'terreno_moneda_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'tiempo_limite': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tipo_adquisicion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tipo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'valor_solicitado_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'valor_solicitado_monedalocal': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'})
        },
        u'db.edificacion_condiciones': {
            'Meta': {'object_name': 'Edificacion_Condiciones'},
            'condicion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Condiciones']"}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.BooleanField', [], {})
        },
        u'db.fuentes_financieras': {
            'Meta': {'object_name': 'Fuentes_Financieras'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valor_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'valor_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'})
        },
        u'db.preguntas': {
            'Meta': {'object_name': 'Preguntas'},
            'construccion': ('django.db.models.fields.BooleanField', [], {}),
            'construccion1': ('django.db.models.fields.BooleanField', [], {}),
            'construccion2': ('django.db.models.fields.BooleanField', [], {}),
            'construccion3': ('django.db.models.fields.BooleanField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['db']