# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0054_auto_20170705_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_fecha_1',
            field=models.CharField(max_length=30, verbose_name=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_lugar_1',
            field=models.CharField(max_length=30, verbose_name=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_nombre_1',
            field=models.CharField(max_length=30, verbose_name=b'', choices=[(b'Grupo de vida', b'Grupo de vida'), (b'Iglesia hija', b'Iglesia hija'), (b'Proyecto Misionero', b'Proyecto Misionero')]),
            preserve_default=True,
        ),
    ]
