# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0060_remove_informesemestralpublico_plantacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestralpublico',
            name='municipio',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
