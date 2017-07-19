# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0061_informesemestralpublico_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='bautismos_nuevos',
            field=models.PositiveIntegerField(help_text=b'Total de personas bautizadas en el \xc3\xbaltimo semestre', verbose_name=b'Total Bautismos'),
            preserve_default=True,
        ),
    ]
