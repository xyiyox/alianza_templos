# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0062_auto_20170719_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='icm_pin',
            field=models.CharField(max_length=40, null=True, verbose_name=b'Pin de ICM', blank=True),
            preserve_default=True,
        ),
    ]
