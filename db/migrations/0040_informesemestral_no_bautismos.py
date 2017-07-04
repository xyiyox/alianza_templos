# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0039_auto_20170630_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestral',
            name='no_bautismos',
            field=models.TextField(help_text=b'Explique por que no hubo bautismos', null=True, verbose_name=b'Si no hubo bautismos', blank=True),
            preserve_default=True,
        ),
    ]
