# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Congregacion.asistentes_ninos'
        db.delete_column(u'db_congregacion', 'asistentes_ninos')

        # Deleting field 'Congregacion.numero_hijos'
        db.delete_column(u'db_congregacion', 'numero_hijos')

        # Deleting field 'Congregacion.asistentes_adultos'
        db.delete_column(u'db_congregacion', 'asistentes_adultos')

        # Deleting field 'Congregacion.ingresos_ofrendas'
        db.delete_column(u'db_congregacion', 'ingresos_ofrendas')

        # Adding field 'Congregacion.asistencia_general'
        db.add_column(u'db_congregacion', 'asistencia_general',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Congregacion.asistencia_ninos'
        db.add_column(u'db_congregacion', 'asistencia_ninos',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Congregacion.ingreso_mensual'
        db.add_column(u'db_congregacion', 'ingreso_mensual',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=15, decimal_places=3),
                      keep_default=False)

        # Adding field 'Congregacion.cant_hijos'
        db.add_column(u'db_congregacion', 'cant_hijos',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Congregacion.entrenamiento_biblico'
        db.alter_column(u'db_congregacion', 'entrenamiento_biblico', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

        # Changing field 'Congregacion.titulos_obtenidos'
        db.alter_column(u'db_congregacion', 'titulos_obtenidos', self.gf('django.db.models.fields.CharField')(max_length=70))
        # Deleting field 'Comunidad.distancia_ciudad'
        db.delete_column(u'db_comunidad', 'distancia_ciudad')

        # Deleting field 'Comunidad.pais'
        db.delete_column(u'db_comunidad', 'pais')

        # Deleting field 'Comunidad.distancia_iglesia'
        db.delete_column(u'db_comunidad', 'distancia_iglesia')

        # Deleting field 'Comunidad.ciudad_cercana'
        db.delete_column(u'db_comunidad', 'ciudad_cercana')

        # Deleting field 'Comunidad.iglesia_cercana'
        db.delete_column(u'db_comunidad', 'iglesia_cercana')

        # Adding field 'Comunidad.capital_depto'
        db.add_column(u'db_comunidad', 'capital_depto',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Comunidad.distancia_capital'
        db.add_column(u'db_comunidad', 'distancia_capital',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Congregacion.asistentes_ninos'
        db.add_column(u'db_congregacion', 'asistentes_ninos',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Congregacion.numero_hijos'
        db.add_column(u'db_congregacion', 'numero_hijos',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Congregacion.asistentes_adultos'
        db.add_column(u'db_congregacion', 'asistentes_adultos',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Congregacion.ingresos_ofrendas'
        db.add_column(u'db_congregacion', 'ingresos_ofrendas',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=15, decimal_places=3),
                      keep_default=False)

        # Deleting field 'Congregacion.asistencia_general'
        db.delete_column(u'db_congregacion', 'asistencia_general')

        # Deleting field 'Congregacion.asistencia_ninos'
        db.delete_column(u'db_congregacion', 'asistencia_ninos')

        # Deleting field 'Congregacion.ingreso_mensual'
        db.delete_column(u'db_congregacion', 'ingreso_mensual')

        # Deleting field 'Congregacion.cant_hijos'
        db.delete_column(u'db_congregacion', 'cant_hijos')


        # Changing field 'Congregacion.entrenamiento_biblico'
        db.alter_column(u'db_congregacion', 'entrenamiento_biblico', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Congregacion.titulos_obtenidos'
        db.alter_column(u'db_congregacion', 'titulos_obtenidos', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding field 'Comunidad.distancia_ciudad'
        db.add_column(u'db_comunidad', 'distancia_ciudad',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Comunidad.pais'
        db.add_column(u'db_comunidad', 'pais',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=20),
                      keep_default=False)

        # Adding field 'Comunidad.distancia_iglesia'
        db.add_column(u'db_comunidad', 'distancia_iglesia',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Comunidad.ciudad_cercana'
        db.add_column(u'db_comunidad', 'ciudad_cercana',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'Comunidad.iglesia_cercana'
        db.add_column(u'db_comunidad', 'iglesia_cercana',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Deleting field 'Comunidad.capital_depto'
        db.delete_column(u'db_comunidad', 'capital_depto')

        # Deleting field 'Comunidad.distancia_capital'
        db.delete_column(u'db_comunidad', 'distancia_capital')


    models = {
        u'db.adjuntos': {
            'Meta': {'object_name': 'Adjuntos'},
            'archivo_adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_archivo': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'db.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'capital_depto': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'distancia_capital': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'asistencia_general': ('django.db.models.fields.SmallIntegerField', [], {}),
            'asistencia_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'cant_hijos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            'entrenamiento_biblico': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'estado_civil': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fecha_fundacion': ('django.db.models.fields.DateField', [], {}),
            'foto_pastor': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'hay_material': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso_mensual': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'lengua_primaria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'miembros_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'miembros_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre_pastor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'q1_why_not': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q2_how_do': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q2_why_not': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulos_obtenidos': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'usa_material': ('django.db.models.fields.BooleanField', [], {})
        },
        u'db.edificacion': {
            'Meta': {'object_name': 'Edificacion'},
            'coordenadas': ('djgeojson.fields.PointField', [], {}),
            'dimensiones_edificio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_terreno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.SmallIntegerField', [], {}),
            'foto_construccion': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metodo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'nombre_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'num_pisos': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'owner_lote': ('django.db.models.fields.SmallIntegerField', [], {}),
            'requiere_permiso': ('django.db.models.fields.BooleanField', [], {}),
            'tiempo_limite': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tipo_adquisicion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tipo_construccion': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'db.fuentes_financieras': {
            'Meta': {'object_name': 'Fuentes_Financieras'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'})
        },
        u'db.informacionfinanciera': {
            'Meta': {'object_name': 'InformacionFinanciera'},
            'costo_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'dinero_efectivo': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mano_obra': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'valor_materiales': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'valor_solicitado': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '3'}),
            'valor_terreno': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'})
        }
    }

    complete_apps = ['db']