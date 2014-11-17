# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('tipo', models.CharField(help_text=b'Escoja bien el tipo de usuario que desea crear', max_length=10, choices=[(b'superadmin', b'Superadmin'), (b'nacional', b'Nacional'), (b'regional', b'Regional'), (b'local', b'Local'), (b'ingeniero', b'Ingeniero'), (b'arquitecto', b'Arquitecto'), (b'tesorero', b'Tesorero')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_creador', models.ForeignKey(related_name='creador', verbose_name=b'Creado por', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_padre', models.ForeignKey(related_name='padre', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'Asigne este usuario a un usuario regional', null=True, verbose_name=b'Asignado a')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
