# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0042_auto_20170704_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestral',
            name='ofrendas',
            field=models.PositiveIntegerField(default=0, help_text=b'Total dinero recaudado en ofrendas y diezmos', verbose_name=b'Ofrendas y Diezmos'),
            preserve_default=False,
        ),
    ]
