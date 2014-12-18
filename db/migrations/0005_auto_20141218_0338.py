# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_auto_20141210_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificacion',
            name='etapa_actual',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Arquitecto/Ingeniero/Tesorero'), (4, 'Creaci\xf3n de Planos'), (5, 'Aprobaci\xf3n Ingeniero'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (9, 'En Espera de Cupo'), (10, 'En Espera de Recursos'), (11, 'En Construcci\xf3n'), (12, 'Esperando Correcciones'), (13, 'Finalizaci\xf3n')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Arquitecto/Ingeniero/Tesorero'), (4, 'Creaci\xf3n de Planos'), (5, 'Aprobaci\xf3n Ingeniero'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (9, 'En Espera de Cupo'), (10, 'En Espera de Recursos'), (11, 'En Construcci\xf3n'), (12, 'Esperando Correcciones'), (13, 'Finalizaci\xf3n')]),
            preserve_default=True,
        ),
    ]
