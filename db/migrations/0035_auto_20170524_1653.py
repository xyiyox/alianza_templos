# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0034_auto_20170524_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congregacion',
            name='email_pastor',
            field=models.CharField(default=' ', max_length=80, verbose_name=b'Email del pastor'),
            preserve_default=False,
        ),
    ]
