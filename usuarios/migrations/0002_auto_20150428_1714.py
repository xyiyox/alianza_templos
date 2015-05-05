# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(help_text=b'Escoja bien el tipo de usuario que desea crear', max_length=10, choices=[(b'superadmin', b'Superadmin'), (b'nacional', b'Nacional'), (b'regional', b'Regional'), (b'local', b'Local'), (b'ingeniero', b'Director de Obra'), (b'arquitecto', b'Arquitecto'), (b'tesorero', b'Tesorero')]),
            preserve_default=True,
        ),
    ]
