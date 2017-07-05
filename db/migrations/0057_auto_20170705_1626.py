# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0056_auto_20170705_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_nombre_1',
            field=models.CharField(max_length=30, verbose_name=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_nombre_2',
            field=models.CharField(max_length=30, verbose_name=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_nombre_3',
            field=models.CharField(max_length=30, verbose_name=b''),
            preserve_default=True,
        ),
    ]
