# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_auto_20150506_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionfinanciera',
            name='banco',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Nombre del Banco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='informacionfinanciera',
            name='tipo_cuenta',
            field=models.SmallIntegerField(default=0, verbose_name=b'Tipo de Cuenta', choices=[(0, b'Ahorros'), (1, b'Corriente')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='informacionfinanciera',
            name='titular_cuenta',
            field=models.CharField(default=b'', help_text=b'Debe ser una cuenta de la Alianza', max_length=100, verbose_name=b'Titular'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='dimensiones_edificio',
            field=models.CharField(help_text=b'Ingrese las medidas en Metros. Para construcci\xc3\xb3n de templos las m\xc3\xa9didas autorizadas son 200 mt cuadrados y para obra social 150 mt cuadrados. Si las m\xc3\xa9didas superan estos valores entonces se asume que la congregaci\xc3\xb3n aporta el excedente del dinero', max_length=30, verbose_name=b'Dimensiones del Edificio'),
            preserve_default=True,
        ),
    ]
