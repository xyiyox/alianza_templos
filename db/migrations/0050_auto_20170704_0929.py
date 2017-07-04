# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0049_auto_20170704_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='uso_local',
            field=models.TextField(default='', help_text=b'Como se uso el local en el \xc3\xbaltimo semestre. ej.: Escuela de d\xc3\xada, entrenamiento vocacional, estudios b\xc3\xadblicos, ministerio de mujeres, proyecci\xc3\xb3n de pel\xc3\xadculas etc.', verbose_name=b'Uso del local de la iglesia'),
            preserve_default=False,
        ),
    ]
