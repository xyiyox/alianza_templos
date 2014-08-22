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
            ('coordenadas', self.gf('map_field.fields.GeoLocationField')(max_length=100)),
            ('owner_lote', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tipo_adquisicion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('dimensiones_terreno', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dimensiones_edificio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('num_pisos', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('tipo_construccion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('metodo_construccion', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('requiere_permiso', self.gf('django.db.models.fields.BooleanField')()),
            ('tiempo_limite', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('estado', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Usuario'])),
        ))
        db.send_create_signal(u'db', ['Edificacion'])

        # Adding model 'InformacionFinanciera'
        db.create_table(u'db_informacionfinanciera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mano_obra', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('valor_materiales', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('dinero_efectivo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('valor_terreno', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('valor_solicitado', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('costo_total', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('edificacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['db.Edificacion'], unique=True)),
        ))
        db.send_create_signal(u'db', ['InformacionFinanciera'])

        # Adding model 'Comunidad'
        db.create_table(u'db_comunidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('poblacion_comunidad', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('capital_depto', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('distancia_capital', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('edificacion', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['db.Edificacion'], unique=True)),
        ))
        db.send_create_signal(u'db', ['Comunidad'])

        # Adding model 'Congregacion'
        db.create_table(u'db_congregacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fecha_fundacion', self.gf('django.db.models.fields.DateField')()),
            ('lengua_primaria', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('region', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('asistencia_general', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('asistencia_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('miembros_adultos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('miembros_ninos', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('ingreso_mensual', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('nombre_pastor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado_civil', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('cant_hijos', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('entrenamiento_biblico', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('titulos_obtenidos', self.gf('django.db.models.fields.CharField')(max_length=70)),
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

        # Adding model 'Fuentes_Financiacion'
        db.create_table(u'db_fuentes_financiacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('info_financiera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.InformacionFinanciera'])),
        ))
        db.send_create_signal(u'db', ['Fuentes_Financiacion'])

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
            ('edificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Edificacion'])),
            ('foto_construccion', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('foto_congregacion', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('foto_pastor', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('permiso_construccion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('escritura_terreno', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('plan_terreno', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('plan_construccion', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('historia_congregacion', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('testimonio_pastor', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'db', ['Adjuntos'])


    def backwards(self, orm):
        # Deleting model 'Edificacion'
        db.delete_table(u'db_edificacion')

        # Deleting model 'InformacionFinanciera'
        db.delete_table(u'db_informacionfinanciera')

        # Deleting model 'Comunidad'
        db.delete_table(u'db_comunidad')

        # Deleting model 'Congregacion'
        db.delete_table(u'db_congregacion')

        # Deleting model 'Fuentes_Financiacion'
        db.delete_table(u'db_fuentes_financiacion')

        # Deleting model 'Condiciones'
        db.delete_table(u'db_condiciones')

        # Deleting model 'Adjuntos'
        db.delete_table(u'db_adjuntos')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'tipo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Usuario']"})
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
        },
        u'usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['db']