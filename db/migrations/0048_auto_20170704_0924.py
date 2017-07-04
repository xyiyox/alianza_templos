# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0047_auto_20170704_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='testimonios',
            field=models.TextField(default='', help_text=b'liberaciones, conversiones, milagros, etc. Favor relatar brevemente el testimonio detallando quien como y donde', verbose_name=b'Testimonios'),
            preserve_default=False,
        ),
    ]
