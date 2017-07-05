# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0053_auto_20170704_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_fecha_1',
            field=models.DateField(default=datetime.datetime(2017, 7, 5, 16, 55, 34, 214823, tzinfo=utc), verbose_name=b'Fecha'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_lugar_1',
            field=models.CharField(default='', max_length=30, verbose_name=b'Lugar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informesemestral',
            name='plantacion_nombre_1',
            field=models.CharField(default='', max_length=30, verbose_name=b'Nombre', choices=[(b'Grupo de vida', b'Grupo de vida'), (b'Iglesia hija', b'Iglesia hija'), (b'Proyecto Misionero', b'Proyecto Misionero')]),
            preserve_default=False,
        ),
    ]
