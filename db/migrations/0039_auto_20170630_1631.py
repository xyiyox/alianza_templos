# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0038_informesemestral_conversiones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='miembros_actuales',
            field=models.PositiveIntegerField(default=0, help_text=b'Bautizados', verbose_name=b'Miembros Actuales'),
            preserve_default=False,
        ),
    ]
