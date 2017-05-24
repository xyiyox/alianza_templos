# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0035_auto_20170524_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidad',
            name='iglesia_cercana',
            field=models.CharField(help_text=b'Iglesia m\xc3\xa1s cercana al proyecto.', max_length=50, verbose_name=b'Iglesia m\xc3\xa1s cercana'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='celular_pastor',
            field=models.CharField(help_text=b'Si no tiene celular, ponga un n\xc3\xbamero de contacto.', max_length=20, verbose_name=b'Celular del pastor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='email_pastor',
            field=models.CharField(help_text=b'Crear correo electr\xc3\xb3nico nuevo o poner el mismo de esta cuenta.', max_length=80, verbose_name=b'Email del pastor'),
            preserve_default=True,
        ),
    ]
