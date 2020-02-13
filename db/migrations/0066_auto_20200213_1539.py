# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0065_auto_20180913_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congregacion',
            name='region',
            field=models.SmallIntegerField(default=0, help_text=b'La Regi\xc3\xb3n a la que pertenece la Iglesia', verbose_name=b'Regi\xc3\xb3n', choices=[(0, b'Central'), (1, b'Sur Oriental'), (2, b'Mecusab'), (3, b'Pac\xc3\xadfico'), (4, b'Sur'), (5, b'Valle'), (6, b'Gu\xc3\xa1mbianos'), (7, b'Paez'), (8, b'Bautista')]),
            preserve_default=True,
        ),
    ]
