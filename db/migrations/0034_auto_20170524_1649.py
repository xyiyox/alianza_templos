# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0033_auto_20170524_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congregacion',
            name='celular_pastor',
            field=models.CharField(default=' ', max_length=20, verbose_name=b'Celular del pastor'),
            preserve_default=False,
        ),
    ]
