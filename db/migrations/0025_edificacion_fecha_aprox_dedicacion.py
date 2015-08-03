# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0024_auto_20150728_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='fecha_aprox_dedicacion',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
