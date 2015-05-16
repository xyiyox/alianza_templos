# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0019_adjuntos_planos_ingeniero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificacion',
            name='aprobacion_arquitecto',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
