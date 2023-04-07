# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_edificacion_aprobacion_tesorero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('etapa', models.IntegerField(max_length=2, choices=[(0, b'Diligenciamiento'), (1, b'Aprobaci\xc3\xb3n Regional'), (2, b'Asignaci\xc3\xb3n de Ingeniero/Arquitecto'), (3, b'Creaci\xc3\xb3n de Planos'), (4, b'Aprobaci\xc3\xb3n Ingeniero'), (5, b'Aprobaci\xc3\xb3n Tesorero'), (6, b'Aprobaci\xc3\xb3n Nacional'), (7, b'Aprobaci\xc3\xb3n Internacional'), (8, b'En Espera de Cupo'), (9, b'En Espera de Recursos'), (10, b'En Construcci\xc3\xb3n'), (11, b'Esperando Correcciones'), (12, b'Finalizaci\xc3\xb3n')])),
                ('created', models.DateField(auto_now_add=True)),
                ('edificacion', models.ForeignKey(to='db.Edificacion', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='edificacion',
            name='created',
            field=models.DateField(default='2014-05-06', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='updated',
            field=models.DateField(default='2014-07-07', auto_now=True),
            preserve_default=False,
        ),
    ]
