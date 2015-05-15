# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0017_auto_20150512_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edificacion',
            name='requiere_arquitecto',
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='etapa_actual',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos')]),
            preserve_default=True,
        ),
    ]
