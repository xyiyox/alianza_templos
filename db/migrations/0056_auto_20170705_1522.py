# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0055_auto_20170705_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_fecha_2',
            field=models.CharField(default='', max_length=30, verbose_name=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_fecha_3',
            field=models.CharField(default='', max_length=30, verbose_name=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_lugar_2',
            field=models.CharField(default='', max_length=30, verbose_name=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_lugar_3',
            field=models.CharField(default='', max_length=30, verbose_name=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_nombre_2',
            field=models.CharField(default='', max_length=30, verbose_name=b'', choices=[(b'Grupo de vida', b'Grupo de vida'), (b'Iglesia hija', b'Iglesia hija'), (b'Proyecto Misionero', b'Proyecto Misionero')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_nombre_3',
            field=models.CharField(default='', max_length=30, verbose_name=b'', choices=[(b'Grupo de vida', b'Grupo de vida'), (b'Iglesia hija', b'Iglesia hija'), (b'Proyecto Misionero', b'Proyecto Misionero')]),
            preserve_default=False,
        ),
    ]
