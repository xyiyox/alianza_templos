# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Preguntas'
        db.delete_table(u'db_preguntas')

        # Deleting model 'Edificacion_Condiciones'
        db.delete_table(u'db_edificacion_condiciones')

        # Deleting field 'Condiciones.descripcion'
        db.delete_column(u'db_condiciones', 'descripcion')

        # Deleting field 'Condiciones.nombre'
        db.delete_column(u'db_condiciones', 'nombre')

        # Adding field 'Condiciones.construccion'
        db.add_column(u'db_condiciones', 'construccion',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.mantenimiento'
        db.add_column(u'db_condiciones', 'mantenimiento',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.actividades'
        db.add_column(u'db_condiciones', 'actividades',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.discipulado'
        db.add_column(u'db_condiciones', 'discipulado',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.alcance'
        db.add_column(u'db_condiciones', 'alcance',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.found_trust'
        db.add_column(u'db_condiciones', 'found_trust',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.found_commitment'
        db.add_column(u'db_condiciones', 'found_commitment',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.found_payment'
        db.add_column(u'db_condiciones', 'found_payment',
                      self.gf('django.db.models.fields.CharField')(default='100%', max_length=20),
                      keep_default=False)

        # Adding field 'Condiciones.presupuesto'
        db.add_column(u'db_condiciones', 'presupuesto',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.terminacion'
        db.add_column(u'db_condiciones', 'terminacion',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.comentarios'
        db.add_column(u'db_condiciones', 'comentarios',
                      self.gf('django.db.models.fields.TextField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.aceptacion'
        db.add_column(u'db_condiciones', 'aceptacion',
                      self.gf('django.db.models.fields.BooleanField')(default=1),
                      keep_default=False)

        # Adding field 'Condiciones.nombre_completo'
        db.add_column(u'db_condiciones', 'nombre_completo',
                      self.gf('django.db.models.fields.CharField')(default='diego bolivar', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Preguntas'
        db.create_table(u'db_preguntas', (
            ('edificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Edificacion'])),
            ('alcance', self.gf('django.db.models.fields.BooleanField')()),
            ('actividades', self.gf('django.db.models.fields.BooleanField')()),
            ('mantenimiento', self.gf('django.db.models.fields.BooleanField')()),
            ('discipulado', self.gf('django.db.models.fields.BooleanField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('construccion', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'db', ['Preguntas'])

        # Adding model 'Edificacion_Condiciones'
        db.create_table(u'db_edificacion_condiciones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('condicion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Condiciones'])),
            ('respuesta', self.gf('django.db.models.fields.BooleanField')()),
            ('edificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['db.Edificacion'])),
        ))
        db.send_create_signal(u'db', ['Edificacion_Condiciones'])

        # Adding field 'Condiciones.descripcion'
        db.add_column(u'db_condiciones', 'descripcion',
                      self.gf('django.db.models.fields.TextField')(default='hola'),
                      keep_default=False)

        # Adding field 'Condiciones.nombre'
        db.add_column(u'db_condiciones', 'nombre',
                      self.gf('django.db.models.fields.CharField')(default='diego', max_length=40),
                      keep_default=False)

        # Deleting field 'Condiciones.construccion'
        db.delete_column(u'db_condiciones', 'construccion')

        # Deleting field 'Condiciones.mantenimiento'
        db.delete_column(u'db_condiciones', 'mantenimiento')

        # Deleting field 'Condiciones.actividades'
        db.delete_column(u'db_condiciones', 'actividades')

        # Deleting field 'Condiciones.discipulado'
        db.delete_column(u'db_condiciones', 'discipulado')

        # Deleting field 'Condiciones.alcance'
        db.delete_column(u'db_condiciones', 'alcance')

        # Deleting field 'Condiciones.found_trust'
        db.delete_column(u'db_condiciones', 'found_trust')

        # Deleting field 'Condiciones.found_commitment'
        db.delete_column(u'db_condiciones', 'found_commitment')

        # Deleting field 'Condiciones.found_payment'
        db.delete_column(u'db_condiciones', 'found_payment')

        # Deleting field 'Condiciones.presupuesto'
        db.delete_column(u'db_condiciones', 'presupuesto')

        # Deleting field 'Condiciones.terminacion'
        db.delete_column(u'db_condiciones', 'terminacion')

        # Deleting field 'Condiciones.comentarios'
        db.delete_column(u'db_condiciones', 'comentarios')

        # Deleting field 'Condiciones.aceptacion'
        db.delete_column(u'db_condiciones', 'aceptacion')

        # Deleting field 'Condiciones.nombre_completo'
        db.delete_column(u'db_condiciones', 'nombre_completo')


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
            'aceptacion': ('django.db.models.fields.BooleanField', [], {}),
            'actividades': ('django.db.models.fields.BooleanField', [], {}),
            'alcance': ('django.db.models.fields.BooleanField', [], {}),
            'comentarios': ('django.db.models.fields.TextField', [], {}),
            'construccion': ('django.db.models.fields.BooleanField', [], {}),
            'discipulado': ('django.db.models.fields.BooleanField', [], {}),
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
        u'db.fuentes_financieras': {
            'Meta': {'object_name': 'Fuentes_Financieras'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valor_dolares': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'valor_local': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'})
        }
    }

    complete_apps = ['db']