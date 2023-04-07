# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20150428_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', to='auth.Group', blank=True, related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('superadmin', 'Superadmin'), ('nacional', 'Nacional'), ('regional', 'Regional'), ('local', 'Local'), ('ingeniero', 'Director de Obra'), ('arquitecto', 'Arquitecto'), ('tesorero', 'Tesorero')], max_length=10, help_text='Escoja bien el tipo de usuario que desea crear'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_creador',
            field=models.ForeignKey(related_name='creador', to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Creado por', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_padre',
            field=models.ForeignKey(related_name='padre', to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Asignado a', help_text='Asigne este usuario a un usuario regional', on_delete=models.CASCADE),
        ),
    ]
