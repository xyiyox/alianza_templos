# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0040_informesemestral_no_bautismos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='bautismos_nuevos',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Total Bautismos'),
            preserve_default=False,
        ),
    ]
