# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0063_edificacion_icm_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjuntos',
            name='certificacion',
            field=models.FileField(default='ninguno', help_text=b'Agregue certificaci\xc3\xb3n bancaria o de materiales', verbose_name=b'Certificaci\xc3\xb3n', upload_to=db.models.calcular_ruta),
            preserve_default=False,
        ),
    ]
