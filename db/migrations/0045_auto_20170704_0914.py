# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0044_auto_20170704_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='grupos_vida',
            field=models.PositiveIntegerField(help_text=b'N\xc3\xbamero actual de grupos de vida, grupos evangel\xc3\xadsticos, casas de oraci\xc3\xb3n, grupos peque\xc3\xb1os en casas etc..', verbose_name=b'Grupos de vida o Celulas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion',
            field=models.PositiveIntegerField(default=0, help_text=b'Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas en el \xc3\xbaltimo semestre', verbose_name=b'Plantacion de Iglesias'),
            preserve_default=False,
        ),
    ]
