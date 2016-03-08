# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0028_auto_20160225_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informesemestral',
            options={'verbose_name_plural': 'informes'},
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='asistencia_general',
            field=models.PositiveIntegerField(help_text=b'Incluyendo ni\xc3\xb1os y no bautizados', null=True, verbose_name=b'Total Asistencia General', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='bautismos_nuevos',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Total Bautismos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='grupos_vida',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Numero de Grupos de vida o Celulas', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='informe',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='miembros_actuales',
            field=models.PositiveIntegerField(help_text=b'Bautizados', null=True, verbose_name=b'Miembros Actuales', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='nuevos_miembros',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Total Miembros Nuevos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion',
            field=models.PositiveIntegerField(help_text=b'Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas', null=True, verbose_name=b'Plantacion de Iglesias: Cantidad', blank=True),
            preserve_default=True,
        ),
    ]
