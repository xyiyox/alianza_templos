# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0064_adjuntos_certificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congregacion',
            name='region',
            field=models.SmallIntegerField(default=0, help_text=b'La Regi\xc3\xb3n a la que pertenece la Iglesia', verbose_name=b'Regi\xc3\xb3n', choices=[(0, b'Central'), (1, b'Sur Oriental'), (2, b'Mecusab'), (3, b'Pac\xc3\xadfico'), (4, b'Sur'), (5, b'Valle'), (6, b'Guanbianos'), (7, b'Paez'), (8, b'Bautista')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='owner_lote',
            field=models.SmallIntegerField(default=0, verbose_name=b'Due\xc3\xb1o del Lote', choices=[(0, b'Propio Iglesia Local'), (1, b'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='titular_cuenta',
            field=models.CharField(default=b'', help_text=b'Debe ser una cuenta de la iglesia', max_length=100, verbose_name=b'Titular'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='region',
            field=models.SmallIntegerField(help_text=b'La Regi\xc3\xb3n a la que pertenece la Iglesia', verbose_name=b'Regi\xc3\xb3n', choices=[(0, b'Central'), (1, b'Sur Oriental'), (2, b'Mecusab'), (3, b'Pac\xc3\xadfico'), (4, b'Sur'), (5, b'Valle'), (6, b'Guanbianos'), (7, b'Paez'), (8, b'Bautista')]),
            preserve_default=True,
        ),
    ]
