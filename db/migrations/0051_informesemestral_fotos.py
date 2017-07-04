# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0050_auto_20170704_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='informesemestral',
            name='fotos',
            field=models.FileField(default='', help_text=b'Suba un un archivo comprimido en .Rar o .Zip de fotos que evidencien los programas realizados en el templo', verbose_name=b'Fotos evidencia', upload_to=db.models.ruta_fotos_informe_semestral),
            preserve_default=False,
        ),
    ]
