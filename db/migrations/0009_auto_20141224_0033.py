# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20141222_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjuntos',
            name='planos_arquitecto',
            field=models.FileField(upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Planos'),
            preserve_default=True,
        ),
    ]
