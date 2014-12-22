# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20141218_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjuntos',
            name='planos_arquitecto',
            field=models.FileField(null=True, upload_to=db.models.calcular_ruta, blank=True),
            preserve_default=True,
        ),
    ]
