# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Fuentes_Financieras'
        db.delete_table(u'db_fuentes_financieras')

        # Adding model 'Fuentes_Financiacion'
        db.create_table(u'db_fuentes_financiacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('info_financiera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.InformacionFinanciera'])),
        ))
        db.send_create_signal(u'db', ['Fuentes_Financiacion'])

        # Deleting field 'Congregacion.foto_pastor'
        db.delete_column(u'db_congregacion', 'foto_pastor')

        # Deleting field 'Adjuntos.archivo_adjunto'
        db.delete_column(u'db_adjuntos', 'archivo_adjunto')

        # Deleting field 'Adjuntos.tipo_archivo'
        db.delete_column(u'db_adjuntos', 'tipo_archivo')

        # Adding field 'Adjuntos.edificacion'
        db.add_column(u'db_adjuntos', 'edificacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['db.Edificacion']),
                      keep_default=False)

        # Adding field 'Adjuntos.foto_construccion'
        db.add_column(u'db_adjuntos', 'foto_construccion',
                      self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.foto_congregacion'
        db.add_column(u'db_adjuntos', 'foto_congregacion',
                      self.gf('django.db.models.fields.files.ImageField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.foto_pastor'
        db.add_column(u'db_adjuntos', 'foto_pastor',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.permiso_construccion'
        db.add_column(u'db_adjuntos', 'permiso_construccion',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.escritura_terreno'
        db.add_column(u'db_adjuntos', 'escritura_terreno',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.plan_terreno'
        db.add_column(u'db_adjuntos', 'plan_terreno',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.plan_construccion'
        db.add_column(u'db_adjuntos', 'plan_construccion',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.historia_congregacion'
        db.add_column(u'db_adjuntos', 'historia_congregacion',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.testimonio_pastor'
        db.add_column(u'db_adjuntos', 'testimonio_pastor',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Fuentes_Financieras'
        db.create_table(u'db_fuentes_financieras', (
            ('edificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Edificacion'])),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'db', ['Fuentes_Financieras'])

        # Deleting model 'Fuentes_Financiacion'
        db.delete_table(u'db_fuentes_financiacion')

        # Adding field 'Congregacion.foto_pastor'
        db.add_column(u'db_congregacion', 'foto_pastor',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.archivo_adjunto'
        db.add_column(u'db_adjuntos', 'archivo_adjunto',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Adjuntos.tipo_archivo'
        db.add_column(u'db_adjuntos', 'tipo_archivo',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Adjuntos.edificacion'
        db.delete_column(u'db_adjuntos', 'edificacion_id')

        # Deleting field 'Adjuntos.foto_construccion'
        db.delete_column(u'db_adjuntos', 'foto_construccion')

        # Deleting field 'Adjuntos.foto_congregacion'
        db.delete_column(u'db_adjuntos', 'foto_congregacion')

        # Deleting field 'Adjuntos.foto_pastor'
        db.delete_column(u'db_adjuntos', 'foto_pastor')

        # Deleting field 'Adjuntos.permiso_construccion'
        db.delete_column(u'db_adjuntos', 'permiso_construccion')

        # Deleting field 'Adjuntos.escritura_terreno'
        db.delete_column(u'db_adjuntos', 'escritura_terreno')

        # Deleting field 'Adjuntos.plan_terreno'
        db.delete_column(u'db_adjuntos', 'plan_terreno')

        # Deleting field 'Adjuntos.plan_construccion'
        db.delete_column(u'db_adjuntos', 'plan_construccion')

        # Deleting field 'Adjuntos.historia_congregacion'
        db.delete_column(u'db_adjuntos', 'historia_congregacion')

        # Deleting field 'Adjuntos.testimonio_pastor'
        db.delete_column(u'db_adjuntos', 'testimonio_pastor')


    models = {
        u'db.adjuntos': {
            'Meta': {'object_name': 'Adjuntos'},
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            'escritura_terreno': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'foto_congregacion': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'foto_construccion': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'foto_pastor': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'historia_congregacion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permiso_construccion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'plan_construccion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
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