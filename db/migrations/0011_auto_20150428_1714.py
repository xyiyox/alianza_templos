# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20150423_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='requiere_arquitecto',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='distancia_capital',
            field=models.PositiveSmallIntegerField(help_text=b'Por favor ingrese el valor en Kilometros (Km)', verbose_name=b'Distancia del Proyecto a la capital'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='poblacion_comunidad',
            field=models.CharField(max_length=40, verbose_name=b'Poblaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='estado_civil',
            field=models.SmallIntegerField(default=0, verbose_name=b'Estado civil', choices=[(0, b'Soltero'), (1, b'Casado'), (2, b'Viudo'), (3, b'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='fecha_fundacion',
            field=models.DateField(verbose_name=b'Fecha de Fundaci\xc3\xb3n de la Congregacion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='lengua_primaria',
            field=models.CharField(max_length=20, verbose_name=b'Lengua Materna'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='region',
            field=models.SmallIntegerField(default=0, help_text=b'La Regi\xc3\xb3n a la que pertenece la Iglesia', verbose_name=b'Regi\xc3\xb3n', choices=[(0, b'Central'), (1, b'Sur Oriental'), (2, b'Mecusab'), (3, b'Pac\xc3\xadfico'), (4, b'Sur'), (5, b'Valle'), (6, b'Guanbianos')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='titulos_obtenidos',
            field=models.CharField(max_length=50, verbose_name=b'Titulos obtenidos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='etapa_actual',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Arquitecto/Director de Obra/Tesorero'), (4, 'Creaci\xf3n de Planos'), (5, 'Aprobaci\xf3n Director de Obra'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (9, 'En Espera de Cupo'), (10, 'En Espera de Recursos'), (11, 'En Construcci\xf3n'), (12, 'Esperando Correcciones'), (13, 'Finalizaci\xf3n')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='ingeniero',
            field=models.ForeignKey(related_name='ingeniero', verbose_name=b'Maestro de Obra Asignado', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='metodo_construccion',
            field=models.SmallIntegerField(default=0, verbose_name=b'M\xc3\xa9todo de Construcci\xc3\xb3n', choices=[(0, b'Nueva Edificacion'), (1, b'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='owner_lote',
            field=models.SmallIntegerField(default=0, verbose_name=b'Due\xc3\xb1o del Lote', choices=[(0, b'Alianza Cristiana'), (1, b'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='requiere_permiso',
            field=models.BooleanField(default=True, verbose_name=b'\xc2\xbfRequiere permiso de construcci\xc3\xb3n?', choices=[(True, b'Si'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_adquisicion',
            field=models.SmallIntegerField(default=0, verbose_name=b'M\xc3\xa9todo de Adquisici\xc3\xb3n', choices=[(0, b'Comprado'), (1, b'Donado')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_construccion',
            field=models.SmallIntegerField(default=0, verbose_name=b'Tipo de Construcci\xc3\xb3n', choices=[(0, b'Iglesia'), (1, b'Guarderia'), (2, b'Iglesia/Guarderia')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Arquitecto/Director de Obra/Tesorero'), (4, 'Creaci\xf3n de Planos'), (5, 'Aprobaci\xf3n Director de Obra'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (9, 'En Espera de Cupo'), (10, 'En Espera de Recursos'), (11, 'En Construcci\xf3n'), (12, 'Esperando Correcciones'), (13, 'Finalizaci\xf3n')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='dinero_efectivo',
            field=models.PositiveIntegerField(help_text=b'Ingrese el valor en Pesos Colombianos (COP), El total con el que cuenta Fisicamente', verbose_name=b'Dinero Ahorrado'),
            preserve_default=True,
        ),
    ]
