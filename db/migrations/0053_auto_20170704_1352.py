# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0052_auto_20170704_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='fotos',
            field=models.FileField(help_text=b'Suba un un archivo comprimido en .rar o .zip de fotos que evidencien los programas realizados en el templo', upload_to=db.models.ruta_fotos_informe_semestral, verbose_name=b'Fotos evidencia', validators=[db.models.validate_comprimidos]),
            preserve_default=True,
        ),
    ]
