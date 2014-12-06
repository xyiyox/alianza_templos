# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20141206_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='aprobacion_tesorero',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
