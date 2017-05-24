# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0031_auto_20160308_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidad',
            name='poblacion_comunidad',
            field=models.CharField(help_text=b'Cantidad de habitantes en n\xc3\xbamero', max_length=40, verbose_name=b'Poblaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='region',
            field=models.SmallIntegerField(default=0, help_text=b'La Regi\xc3\xb3n a la que pertenece la Iglesia', verbose_name=b'Regi\xc3\xb3n', choices=[(0, b'Central'), (1, b'Sur Oriental'), (2, b'Mecusab'), (3, b'Pac\xc3\xadfico'), (4, b'Sur'), (5, b'Valle'), (6, b'Guanbianos'), (7, b'Paez')]),
            preserve_default=True,
        ),
    ]
