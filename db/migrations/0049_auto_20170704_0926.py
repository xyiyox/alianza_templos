# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0048_auto_20170704_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='ministerio_ninos',
            field=models.TextField(default='', help_text=b'Describa las \xc3\xbaltimas actividades con ni\xc3\xb1os en el \xc3\xbaltimo semestre como: campamentos, alcances evangelisticos, escuela b\xc3\xadblica, deportes,grupos de vida, etc.', verbose_name=b'Ministerio de los Ni\xc3\xb1os'),
            preserve_default=False,
        ),
    ]
