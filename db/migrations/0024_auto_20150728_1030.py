# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0023_auto_20150724_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjuntos',
            name='dedicacion',
            field=models.FileField(upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Dedicacion Comprimido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='fotos_p1',
            field=models.FileField(upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Comprimido de Fotos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='fotos_p2',
            field=models.FileField(upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Comprimido de Fotos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='fotos_p3',
            field=models.FileField(upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Comprimido de Fotos'),
            preserve_default=True,
        ),        
        migrations.AlterField(
            model_name='edificacion',
            name='etapa_actual',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_construccion',
            field=models.SmallIntegerField(default=0, help_text=b'Seleccione el tipo de Construccion, Tenga encuenta para el caso de Templo/Obra Social de identificar como se va construir esta instalacion, esta informacion es importante y debe ser precisa', verbose_name=b'Tipo de Construcci\xc3\xb3n', choices=[(0, b'Templo'), (1, b'Obra Social'), (2, b'Templo/Obra Social (Arriba)'), (3, b'Templo/Obra Social (Lateral)'), (4, b'Templo/Obra Social (Atras)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plazo',
            name='etapa',
            field=models.PositiveSmallIntegerField(unique=True, max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion')]),
            preserve_default=True,
        ),
    ]
