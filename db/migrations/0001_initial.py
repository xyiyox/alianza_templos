# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Edificacion'
        db.create_table(u'db_edificacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_proyecto', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('coordenadas', self.gf('djgeojson.fields.PointField')()),
            ('owner_escritura', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tipo_adquisicion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tiempo_limite', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('dimensiones_terreno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dimensiones_edificio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tipo_construccion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('metodo_construccion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('requiere_permiso', self.gf('django.db.models.fields.BooleanField')()),
            ('is_icm_approved', self.gf('django.db.models.fields.BooleanField')()),
            ('moneda_local', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mano_obra', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('valor_materiales', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('dinero_efectivo', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('aporte_terreno', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('valor_solicitado', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('costo_total', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3)),
            ('pago_fondo', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('estado', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'db', ['Edificacion'])

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
            ('edificacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['db.Edificacion'], unique=True)),
        ))
        db.send_create_signal(u'db', ['Comunidad'])

        # Adding model 'Congregacion'
        db.create_table(u'db_congregacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lengua_primaria', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fecha_fundacion', self.gf('django.db.models.fields.DateField')()),
            ('asistentes_adultos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('asistentes_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('miembros_adultos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('miembros_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('ingresos_ofrendas', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('nombre_pastor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('entrenamiento_biblico', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado_civil', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('numero_hijos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('titulos_obtenidos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('anios_iglesia', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('anios_ministerio', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('hay_material', self.gf('django.db.models.fields.BooleanField')()),
            ('q1_why_not', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('usa_material', self.gf('django.db.models.fields.BooleanField')()),
            ('q2_why_not', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('q2_how_do', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('edificacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['db.Edificacion'], unique=True)),
        ))
        db.send_create_signal(u'db', ['Congregacion'])

        # Adding model 'Fuentes_Financieras'
        db.create_table(u'db_fuentes_financieras', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('edificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Edificacion'])),
        ))
        db.send_create_signal(u'db', ['Fuentes_Financieras'])

        # Adding model 'Condiciones'
        db.create_table(u'db_condiciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('edificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Edificacion'])),
            ('construccion', self.gf('django.db.models.fields.BooleanField')()),
            ('mantenimiento', self.gf('django.db.models.fields.BooleanField')()),
            ('actividades', self.gf('django.db.models.fields.BooleanField')()),
            ('discipulado', self.gf('django.db.models.fields.BooleanField')()),
            ('alcance', self.gf('django.db.models.fields.BooleanField')()),
            ('found_trust', self.gf('django.db.models.fields.BooleanField')()),
            ('found_commitment', self.gf('django.db.models.fields.BooleanField')()),
            ('found_payment', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('presupuesto', self.gf('django.db.models.fields.BooleanField')()),
            ('terminacion', self.gf('django.db.models.fields.BooleanField')()),
            ('comentarios', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('aceptacion', self.gf('django.db.models.fields.BooleanField')()),
            ('nombre_completo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'db', ['Condiciones'])

        # Adding model 'Adjuntos'
        db.create_table(u'db_adjuntos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_archivo', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('archivo_adjunto', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'db', ['Adjuntos'])


    def backwards(self, orm):
        # Deleting model 'Edificacion'
        db.delete_table(u'db_edificacion')

        # Deleting model 'Comunidad'
        db.delete_table(u'db_comunidad')

        # Deleting model 'Congregacion'
        db.delete_table(u'db_congregacion')

        # Deleting model 'Fuentes_Financieras'
        db.delete_table(u'db_fuentes_financieras')

        # Deleting model 'Condiciones'
        db.delete_table(u'db_condiciones')

        # Deleting model 'Adjuntos'
        db.delete_table(u'db_adjuntos')


    models = {
        u'db.adjuntos': {
            'Meta': {'object_name': 'Adjuntos'},
            'archivo_adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_archivo': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'db.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'ciudad_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'distancia_ciudad': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'distancia_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iglesia_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'poblacion_comunidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'db.condiciones': {
            'Meta': {'object_name': 'Condiciones'},
            'aceptacion': ('django.db.models.fields.BooleanField', [], {}),
            'actividades': ('django.db.models.fields.BooleanField', [], {}),
            'alcance': ('django.db.models.fields.BooleanField', [], {}),
            'comentarios': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'construccion': ('django.db.models.fields.BooleanField', [], {}),
            'discipulado': ('django.db.models.fields.BooleanField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            'found_commitment': ('django.db.models.fields.BooleanField', [], {}),
            'found_payment': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'found_trust': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mantenimiento': ('django.db.models.fields.BooleanField', [], {}),
            'nombre_completo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'presupuesto': ('django.db.models.fields.BooleanField', [], {}),
            'terminacion': ('django.db.models.fields.BooleanField', [], {})
        },
        u'db.congregacion': {
            'Meta': {'object_name': 'Congregacion'},
            'anios_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'anios_ministerio': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'asistentes_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'asistentes_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            'entrenamiento_biblico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estado_civil': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fecha_fundacion': ('django.db.models.fields.DateField', [], {}),
            'hay_material': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos_ofrendas': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'lengua_primaria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'miembros_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'miembros_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre_pastor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero_hijos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'q1_why_not': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q2_how_do': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q2_why_not': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulos_obtenidos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'usa_material': ('django.db.models.fields.BooleanField', [], {})
        },
        u'db.edificacion': {
            'Meta': {'object_name': 'Edificacion'},
            'aporte_terreno': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'coordenadas': ('djgeojson.fields.PointField', [], {}),
            'costo_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'dimensiones_edificio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_terreno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dinero_efectivo': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_icm_approved': ('django.db.models.fields.BooleanField', [], {}),
            'mano_obra': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'metodo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'moneda_local': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'owner_escritura': ('django.db.models.fields.SmallIntegerField', [], {}),
            'pago_fondo': ('django.db.models.fields.SmallIntegerField', [], {}),
            'requiere_permiso': ('django.db.models.fields.BooleanField', [], {}),
            'tiempo_limite': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tipo_adquisicion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tipo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'valor_materiales': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'valor_solicitado': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'})
        },
        u'db.fuentes_financieras': {
            'Meta': {'object_name': 'Fuentes_Financieras'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'})
        }
    }

    complete_apps = ['db']