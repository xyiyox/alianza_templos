# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0026_auto_20160208_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformeSemestral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('informe', models.SmallIntegerField(null=True, blank=True)),
                ('fecha_elaboracion', models.DateTimeField(auto_now_add=True)),
                ('miembros_actuales', models.PositiveSmallIntegerField(help_text=b'Bautizados', verbose_name=b'Miembros Actuales')),
                ('nuevos_miembros', models.PositiveSmallIntegerField(verbose_name=b'Total Miembros Nuevos')),
                ('bautismos_nuevos', models.PositiveSmallIntegerField(verbose_name=b'Total Bautismos')),
                ('asistencia_general', models.PositiveSmallIntegerField(help_text=b'Incluyendo ni\xc3\xb1os y no bautizados', verbose_name=b'Total Asistencia General')),
                ('grupos_vida', models.PositiveSmallIntegerField(verbose_name=b'Numero de Grupos de vida o Celulas')),
                ('plantacion', models.PositiveSmallIntegerField(help_text=b'Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas', verbose_name=b'Plantacion de Iglesias: Cantidad')),
                ('peticiones_oracion', models.TextField(help_text=b'Especificas, accion de gracias o preocupaciones', verbose_name=b'Peticiones de Oracion')),
                ('testimonios', models.TextField(help_text=b'liberaciones, conversiones, milagros, etc', verbose_name=b'Testimonios')),
                ('ministerio_ninos', models.TextField(help_text=b'Campamentos. alcances evangelisticos, escuela biblica, deportes,grupos de vida, etc.', verbose_name=b'Ministerio de los Ni\xc3\xb1os')),
                ('uso_local', models.TextField(help_text=b'Escuela de dia, entrenamiento vocacional, estudios biblicos, ministerio de mujeres, proyeccion de peliculas, etc.', verbose_name=b'Uso del local de la iglesia')),
                ('edificacion', models.ForeignKey(to='db.Edificacion', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='foto_construccion',
            field=models.ImageField(help_text=b'Mostrando claramente el terreno donde se va a construir la iglesia, jpg o png, minimo 600 x 480 pixeles, Tama\xc3\xb1o maximo 2MB', upload_to=db.models.calcular_ruta, verbose_name=b'Foto del Terreno'),
            preserve_default=True,
        ),
    ]
