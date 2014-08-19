# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'InformacionFinanciera.valor_terreno'
        db.alter_column(u'db_informacionfinanciera', 'valor_terreno', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'InformacionFinanciera.valor_materiales'
        db.alter_column(u'db_informacionfinanciera', 'valor_materiales', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'InformacionFinanciera.mano_obra'
        db.alter_column(u'db_informacionfinanciera', 'mano_obra', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'InformacionFinanciera.valor_solicitado'
        db.alter_column(u'db_informacionfinanciera', 'valor_solicitado', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'InformacionFinanciera.costo_total'
        db.alter_column(u'db_informacionfinanciera', 'costo_total', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'InformacionFinanciera.dinero_efectivo'
        db.alter_column(u'db_informacionfinanciera', 'dinero_efectivo', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Adjuntos.foto_pastor'
        db.alter_column(u'db_adjuntos', 'foto_pastor', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'Adjuntos.plan_construccion'
        db.alter_column(u'db_adjuntos', 'plan_construccion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Changing field 'Adjuntos.permiso_construccion'
        db.alter_column(u'db_adjuntos', 'permiso_construccion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'InformacionFinanciera.valor_terreno'
        db.alter_column(u'db_informacionfinanciera', 'valor_terreno', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3))

        # Changing field 'InformacionFinanciera.valor_materiales'
        db.alter_column(u'db_informacionfinanciera', 'valor_materiales', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3))

        # Changing field 'InformacionFinanciera.mano_obra'
        db.alter_column(u'db_informacionfinanciera', 'mano_obra', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3))

        # Changing field 'InformacionFinanciera.valor_solicitado'
        db.alter_column(u'db_informacionfinanciera', 'valor_solicitado', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3))

        # Changing field 'InformacionFinanciera.costo_total'
        db.alter_column(u'db_informacionfinanciera', 'costo_total', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=3))

        # Changing field 'InformacionFinanciera.dinero_efectivo'
        db.alter_column(u'db_informacionfinanciera', 'dinero_efectivo', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3))

        # Changing field 'Adjuntos.foto_pastor'
        db.alter_column(u'db_adjuntos', 'foto_pastor', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100))

        # Changing field 'Adjuntos.plan_construccion'
        db.alter_column(u'db_adjuntos', 'plan_construccion', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100))

        # Changing field 'Adjuntos.permiso_construccion'
        db.alter_column(u'db_adjuntos', 'permiso_construccion', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100))

    models = {
        u'db.adjuntos': {
            'Meta': {'object_name': 'Adjuntos'},
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            'escritura_terreno': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'foto_congregacion': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'foto_construccion': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'foto_pastor': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'historia_congregacion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permiso_construccion': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'plan_construccion': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'plan_terreno': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testimonio_pastor': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
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
            'region': ('django.db.models.fields.SmallIntegerField', [], {}),
            'titulos_obtenidos': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'usa_material': ('django.db.models.fields.BooleanField', [], {})
        },
        u'db.edificacion': {
            'Meta': {'object_name': 'Edificacion'},
            'coordenadas': ('map_field.fields.GeoLocationField', [], {'max_length': '100'}),
            'dimensiones_edificio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_terreno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.SmallIntegerField', [], {}),
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
        u'db.fuentes_financiacion': {
            'Meta': {'object_name': 'Fuentes_Financiacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_financiera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.InformacionFinanciera']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'})
        },
        u'db.informacionfinanciera': {
            'Meta': {'object_name': 'InformacionFinanciera'},
            'costo_total': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'dinero_efectivo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mano_obra': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'valor_materiales': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'valor_solicitado': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'valor_terreno': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['db']