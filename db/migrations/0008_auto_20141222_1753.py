# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etapa',
            options={'get_latest_by': 'created'},
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='aprobacion_arquitecto',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfDesea Aprobar?'),
            preserve_default=True,
        ),
    ]
