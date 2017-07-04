# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0046_informesemestral_asistencia_grupos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='peticiones_oracion',
            field=models.TextField(default='', help_text=b'Especificas, accion de gracias o preocupaciones, favor explicar o dar detalles de la petici\xc3\xb3n', verbose_name=b'Peticiones de Oracion'),
            preserve_default=False,
        ),
    ]
