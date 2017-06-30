# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0037_auto_20170525_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestral',
            name='conversiones',
            field=models.PositiveIntegerField(default=0, help_text=b'Total de personas que aceptaron a Cristo como su Se\xc3\xb1or y Salvador en el \xc3\xbaltimo semestre', verbose_name=b'Conversiones'),
            preserve_default=False,
        ),
    ]
