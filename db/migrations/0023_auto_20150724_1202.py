# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0022_plazo'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='aprobacion_fotos', 
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='envio_alianza',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='envio_icm',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plazo',
            name='peso',
            field=models.IntegerField(default=1, unique=True, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='etapa_actual',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Cuarta Fase de Construccion'), (15, 'Dedicacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Cuarta Fase de Construccion'), (15, 'Dedicacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plazo',
            name='etapa',
            field=models.PositiveSmallIntegerField(unique=True, max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Cuarta Fase de Construccion'), (15, 'Dedicacion')]),
            preserve_default=True,
        ),
    ]
