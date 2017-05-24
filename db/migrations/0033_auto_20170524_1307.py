# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0032_auto_20170524_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunidad',
            name='distancia_iglesia',
            field=models.PositiveSmallIntegerField(default=0, help_text=b'La iglesia m\xc3\xa1s cercana debe estar minimo a 10 o 15 km. (ingrese valor en kil\xc3\xb3metros)', verbose_name=b'Distancia a la Iglesia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comunidad',
            name='iglesia_cercana',
            field=models.CharField(default=' ', max_length=50, verbose_name=b'Iglesia m\xc3\xa1s cercana'),
            preserve_default=False,
        ),
    ]
