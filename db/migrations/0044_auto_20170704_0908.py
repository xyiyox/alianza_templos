# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0043_informesemestral_ofrendas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='grupos_vida',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Numero de Grupos de vida o Celulas'),
            preserve_default=False,
        ),
    ]
