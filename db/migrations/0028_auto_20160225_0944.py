# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0027_auto_20160224_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='asistencia_general',
            field=models.PositiveSmallIntegerField(help_text=b'Incluyendo ni\xc3\xb1os y no bautizados', null=True, verbose_name=b'Total Asistencia General', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='bautismos_nuevos',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Total Bautismos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='grupos_vida',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Numero de Grupos de vida o Celulas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='miembros_actuales',
            field=models.PositiveSmallIntegerField(help_text=b'Bautizados', null=True, verbose_name=b'Miembros Actuales', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='ministerio_ninos',
            field=models.TextField(help_text=b'Campamentos. alcances evangelisticos, escuela biblica, deportes,grupos de vida, etc.', null=True, verbose_name=b'Ministerio de los Ni\xc3\xb1os', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='nuevos_miembros',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'Total Miembros Nuevos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='peticiones_oracion',
            field=models.TextField(help_text=b'Especificas, accion de gracias o preocupaciones', null=True, verbose_name=b'Peticiones de Oracion', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion',
            field=models.PositiveSmallIntegerField(help_text=b'Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas', null=True, verbose_name=b'Plantacion de Iglesias: Cantidad', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='testimonios',
            field=models.TextField(help_text=b'liberaciones, conversiones, milagros, etc', null=True, verbose_name=b'Testimonios', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='uso_local',
            field=models.TextField(help_text=b'Escuela de dia, entrenamiento vocacional, estudios biblicos, ministerio de mujeres, proyeccion de peliculas, etc.', null=True, verbose_name=b'Uso del local de la iglesia', blank=True),
            preserve_default=True,
        ),
    ]
