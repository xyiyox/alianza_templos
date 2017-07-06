# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0058_informesemestralpublico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='grupos_vida',
            field=models.PositiveIntegerField(help_text=b'N\xc3\xbamero actual de grupos de vida, grupos evangel\xc3\xadsticos, casas de oraci\xc3\xb3n, grupos peque\xc3\xb1os en casas etc..', verbose_name=b'Grupos de vida o C\xc3\xa9lulas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='nombre_proyecto',
            field=models.CharField(max_length=40, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='telefono',
            field=models.CharField(help_text=b'Celular y/o tel\xc3\xa9fono, puede poner ambos separados por coma', max_length=40, verbose_name=b'Tel\xc3\xa9fono'),
            preserve_default=True,
        ),
    ]
