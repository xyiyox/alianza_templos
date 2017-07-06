# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0059_auto_20170706_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informesemestralpublico',
            name='plantacion',
        ),
    ]
