# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0030_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificacion',
            name='etapa_actual',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion'), (15, 'Informes Semestrales')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion'), (15, 'Informes Semestrales')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plazo',
            name='etapa',
            field=models.PositiveSmallIntegerField(unique=True, max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion'), (15, 'Informes Semestrales')]),
            preserve_default=True,
        ),
    ]
