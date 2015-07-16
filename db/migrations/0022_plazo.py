# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0021_auto_20150519_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plazo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('etapa', models.PositiveSmallIntegerField(unique=True, max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Usuarios'), (4, 'Creaci\xf3n de Planos'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos')])),
                ('plazo', models.PositiveSmallIntegerField(help_text=b'plazo en d\xc3\xadas', max_length=4)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
