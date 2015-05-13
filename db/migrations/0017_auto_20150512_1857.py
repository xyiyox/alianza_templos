# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0016_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='planos_creados',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='usuarios_asignados',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
