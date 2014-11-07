# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Edificacion.aprobacion_regional'
        db.add_column(u'db_edificacion', 'aprobacion_regional',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Edificacion.aprobacion_arquitecto'
        db.add_column(u'db_edificacion', 'aprobacion_arquitecto',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Edificacion.aprobacion_ingeniero'
        db.add_column(u'db_edificacion', 'aprobacion_ingeniero',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Edificacion.aprobacion_nacional'
        db.add_column(u'db_edificacion', 'aprobacion_nacional',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Edificacion.aprobacion_regional'
        db.delete_column(u'db_edificacion', 'aprobacion_regional')

        # Deleting field 'Edificacion.aprobacion_arquitecto'
        db.delete_column(u'db_edificacion', 'aprobacion_arquitecto')

        # Deleting field 'Edificacion.aprobacion_ingeniero'
        db.delete_column(u'db_edificacion', 'aprobacion_ingeniero')

        # Deleting field 'Edificacion.aprobacion_nacional'
        db.delete_column(u'db_edificacion', 'aprobacion_nacional')


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
        u'db.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'commenter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Usuario']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'aprobacion_arquitecto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aprobacion_ingeniero': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aprobacion_nacional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'aprobacion_regional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'arquitecto': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'arquitecto'", 'null': 'True', 'to': u"orm['usuarios.Usuario']"}),
            'coordenadas': ('map_field.fields.GeoLocationField', [], {'max_length': '100'}),
            'dimensiones_edificio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_terreno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.SmallIntegerField', [], {}),
            'etapa_actual': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingeniero': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ingeniero'", 'null': 'True', 'to': u"orm['usuarios.Usuario']"}),
            'metodo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'nombre_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'num_pisos': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'owner_lote': ('django.db.models.fields.SmallIntegerField', [], {}),
            'requiere_permiso': ('django.db.models.fields.BooleanField', [], {}),
            'tiempo_limite': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tipo_adquisicion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tipo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usuario'", 'to': u"orm['usuarios.Usuario']"})
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
            'desc_voluntarios': ('django.db.models.fields.TextField', [], {}),
            'dias_donados': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dinero_efectivo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mano_obra': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'num_voluntarios': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
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
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user_creador': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'creador'", 'null': 'True', 'to': u"orm['usuarios.Usuario']"}),
            'user_padre': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'padre'", 'null': 'True', 'to': u"orm['usuarios.Usuario']"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['db']