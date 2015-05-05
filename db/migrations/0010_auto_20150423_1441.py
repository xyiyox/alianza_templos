# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_auto_20141224_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adjuntos',
            name='plan_terreno',
        ),
        migrations.RemoveField(
            model_name='congregacion',
            name='hay_material',
        ),
        migrations.RemoveField(
            model_name='congregacion',
            name='q1_why_not',
        ),
        migrations.RemoveField(
            model_name='congregacion',
            name='q2_how_do',
        ),
        migrations.RemoveField(
            model_name='congregacion',
            name='q2_why_not',
        ),
        migrations.RemoveField(
            model_name='congregacion',
            name='usa_material',
        ),
        migrations.RemoveField(
            model_name='informacionfinanciera',
            name='dias_donados',
        ),
        migrations.RemoveField(
            model_name='informacionfinanciera',
            name='valor_solicitado',
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='manzana_catastral',
            field=models.FileField(help_text=b'Mostrando las dimensiones de la propiedad y la ubicaci\xc3\xb3n de la tierra', upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Manzana Catastral', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='costo_total',
            field=models.PositiveIntegerField(help_text=b'Ingrese el valor en Pesos Colombianos (COP)', verbose_name=b'Costo total del proyecto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='dinero_efectivo',
            field=models.PositiveIntegerField(help_text=b'Ingrese el valor en Pesos Colombianos (COP)', verbose_name=b'Dinero Ahorrado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='valor_terreno',
            field=models.PositiveIntegerField(help_text=b'Ingrese el valor en Pesos Colombianos (COP)', verbose_name=b'Valor del Terreno'),
            preserve_default=True,
        ),
    ]
