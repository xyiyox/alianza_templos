# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0026_auto_20160208_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjuntos',
            name='foto_construccion',
            field=models.ImageField(help_text=b'Mostrando claramente el terreno donde se va a construir la iglesia, jpg o png, minimo 600 x 480 pixeles, Tama\xc3\xb1o maximo 2MB', upload_to=db.models.calcular_ruta, verbose_name=b'Foto del Terreno'),
            preserve_default=True,
        ),
    ]
