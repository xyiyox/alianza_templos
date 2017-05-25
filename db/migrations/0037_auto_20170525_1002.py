# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0036_auto_20170524_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjuntos',
            name='historia_congregacion',
            field=models.FileField(help_text=b'Incluya una breve historia de la congregaci\xc3\xb3n preferiblemente en formato WORD.', upload_to=db.models.calcular_ruta, verbose_name=b'Historia de la congregaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='permiso_construccion',
            field=models.FileField(help_text=b'Debe agregar el permiso de construccion, si no necesida debe agregar la prueba de que no necesita permiso.', upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Permiso de construcci\xc3\xb3n o Certificado de que no necesita Permiso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='testimonio_pastor',
            field=models.FileField(help_text=b'Incluya el testimonio del pastor de la congregaci\xc3\xb3n preferiblemente en formato WORD.', upload_to=db.models.calcular_ruta, verbose_name=b'Testimonio del pastor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='asistencia_general',
            field=models.SmallIntegerField(help_text=b'Incluya adultos y ni\xc3\xb1os.', verbose_name=b'Asistencia general promedio'),
            preserve_default=True,
        ),
    ]
