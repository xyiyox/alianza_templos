# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0041_auto_20170704_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='asistencia_general',
            field=models.PositiveIntegerField(default=0, help_text=b'Servicions dominicales y grupos de vida incluyendo ni\xc3\xb1os y no bautizados', verbose_name=b'Total Asistencia General'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='nuevos_miembros',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Total Miembros Nuevos'),
            preserve_default=False,
        ),
    ]
