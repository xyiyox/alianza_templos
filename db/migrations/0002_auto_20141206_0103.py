# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='tesorero',
            field=models.ForeignKey(related_name='tesorero', verbose_name=b'Tesorero Asignado', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='aceptacion',
            field=models.BooleanField(default=False, help_text='Al aceptar usted reconoce que es responsable de la informaci\xf3n suministrada en cada uno de los pasos anteriores\n\t\t\t\t\t\t\t\ty se compromete el cumplimiento de las condiciones aqui expuestas.', verbose_name=b'He le\xc3\xaddo y estoy de acuerdo con los T\xc3\xa9rminos y Condiciones', validators=[db.models.validate_terminos]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='fecha_fundacion',
            field=models.DateField(verbose_name=b'Fecha de Fundaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='aprobacion_arquitecto',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='aprobacion_ingeniero',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='aprobacion_nacional',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='aprobacion_regional',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
