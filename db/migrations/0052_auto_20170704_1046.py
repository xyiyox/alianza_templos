# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0051_informesemestral_fotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informesemestral',
            name='asistencia_general',
            field=models.PositiveIntegerField(help_text=b'Servicios dominicales y grupos de vida incluyendo ni\xc3\xb1os y no bautizados', verbose_name=b'Total Asistencia General'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='nuevos_miembros',
            field=models.PositiveIntegerField(help_text=b'Total de miembros agregados a la membres\xc3\xada de la iglesia en los \xc3\xbaltimos 6 meses', verbose_name=b'Total Miembros Nuevos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='ofrendas',
            field=models.PositiveIntegerField(help_text=b'Total dinero recaudado en ofrendas y diezmos en el \xc3\xbaltimo semestre', verbose_name=b'Ofrendas y Diezmos'),
            preserve_default=True,
        ),
    ]
