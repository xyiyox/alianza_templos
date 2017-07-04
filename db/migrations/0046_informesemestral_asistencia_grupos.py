# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0045_auto_20170704_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestral',
            name='asistencia_grupos',
            field=models.PositiveIntegerField(default=0, help_text=b'Asistencia promedio (por grupo no general) a los grupos de vida', verbose_name=b'Asistencia grupos de vida'),
            preserve_default=False,
        ),
    ]
