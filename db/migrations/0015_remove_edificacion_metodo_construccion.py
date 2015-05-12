# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0014_auto_20150511_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edificacion',
            name='metodo_construccion',
        ),
    ]
