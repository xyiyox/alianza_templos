# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0057_auto_20170705_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformeSemestralPublico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_proyecto', models.CharField(max_length=40, verbose_name=b'Nombre del Proyecto')),
                ('persona', models.CharField(max_length=40, verbose_name=b'Encargado')),
                ('email', models.EmailField(max_length=255)),
                ('telefono', models.CharField(help_text=b'Celular y/o tel\xc3\xa9fono, puede poner ambos separados por coma', max_length=40, verbose_name=b'Encargado')),
                ('depto', models.CharField(max_length=30, verbose_name=b'Departamento', choices=[(b'Amazonas', b'Amazonas'), (b'Antioquia', b'Antioquia'), (b'Arauca', b'Arauca'), (b'Atlantico', b'Atl\xc3\xa1ntico'), (b'Bolivar', b'Bol\xc3\xadvar'), (b'Boyaca', b'Boyac\xc3\xa1'), (b'Caldas', b'Caldas'), (b'Caqueta', b'Caquet\xc3\xa1'), (b'Casanare', b'Casanare'), (b'Cauca', b'Cauca'), (b'Cesar', b'Cesar'), (b'Choco', b'Choc\xc3\xb3'), (b'Cundinamarca', b'Cundinamarca'), (b'Cordoba', b'C\xc3\xb3rdoba'), (b'Guainia', b'Guain\xc3\xada'), (b'Guaviare', b'Guaviare'), (b'Huila', b'Huila'), (b'La Guajira', b'La Guajira'), (b'Magdalena', b'Magdalena'), (b'Meta', b'Meta'), (b'Narino', b'Nari\xc3\xb1o'), (b'Norte de Santander', b'Norte de Santander'), (b'Putumayo', b'Putumayo'), (b'Quindio', b'Quind\xc3\xado'), (b'Risaralda', b'Risaralda'), (b'San Andres', b'San Andr\xc3\xa9s'), (b'Santander', b'Santander'), (b'Sucre', b'Sucre'), (b'Tolima', b'Tolima'), (b'Valle del Cauca', b'Valle del Cauca'), (b'Vaupes', b'Vaup\xc3\xa9s'), (b'Vichada', b'Vichada')])),
                ('direccion', models.TextField(verbose_name=b'Direcci\xc3\xb3n')),
                ('region', models.SmallIntegerField(help_text=b'La Regi\xc3\xb3n a la que pertenece la Iglesia', verbose_name=b'Regi\xc3\xb3n', choices=[(0, b'Central'), (1, b'Sur Oriental'), (2, b'Mecusab'), (3, b'Pac\xc3\xadfico'), (4, b'Sur'), (5, b'Valle'), (6, b'Guanbianos'), (7, b'Paez')])),
                ('miembros_actuales', models.PositiveIntegerField(help_text=b'Bautizados', verbose_name=b'Miembros Actuales')),
                ('nuevos_miembros', models.PositiveIntegerField(help_text=b'Total de miembros agregados a la membres\xc3\xada de la iglesia en los \xc3\xbaltimos 6 meses', verbose_name=b'Total Miembros Nuevos')),
                ('conversiones', models.PositiveIntegerField(help_text=b'Total de personas que aceptaron a Cristo como su Se\xc3\xb1or y Salvador en el \xc3\xbaltimo semestre', verbose_name=b'Conversiones')),
                ('bautismos_nuevos', models.PositiveIntegerField(verbose_name=b'Total Bautismos')),
                ('no_bautismos', models.TextField(help_text=b'Explique por que no hubo bautismos', null=True, verbose_name=b'Si no hubo bautismos', blank=True)),
                ('asistencia_general', models.PositiveIntegerField(help_text=b'Servicios dominicales y grupos de vida incluyendo ni\xc3\xb1os y no bautizados', verbose_name=b'Total Asistencia General')),
                ('grupos_vida', models.PositiveIntegerField(help_text=b'N\xc3\xbamero actual de grupos de vida, grupos evangel\xc3\xadsticos, casas de oraci\xc3\xb3n, grupos peque\xc3\xb1os en casas etc..', verbose_name=b'Grupos de vida o Celulas')),
                ('plantacion', models.PositiveIntegerField(help_text=b'Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas en el \xc3\xbaltimo semestre', verbose_name=b'Plantacion de Iglesias')),
                ('plantacion_nombre_1', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_lugar_1', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_fecha_1', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_nombre_2', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_lugar_2', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_fecha_2', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_nombre_3', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_lugar_3', models.CharField(max_length=30, verbose_name=b'')),
                ('plantacion_fecha_3', models.CharField(max_length=30, verbose_name=b'')),
                ('asistencia_grupos', models.PositiveIntegerField(help_text=b'Asistencia promedio (por grupo no general) a los grupos de vida', verbose_name=b'Asistencia grupos de vida')),
                ('ofrendas', models.PositiveIntegerField(help_text=b'Total dinero recaudado en ofrendas y diezmos en el \xc3\xbaltimo semestre', verbose_name=b'Ofrendas y Diezmos')),
                ('peticiones_oracion', models.TextField(help_text=b'Especificas, accion de gracias o preocupaciones, favor explicar o dar detalles de la petici\xc3\xb3n', verbose_name=b'Peticiones de Oracion')),
                ('testimonios', models.TextField(help_text=b'liberaciones, conversiones, milagros, etc. Favor relatar brevemente el testimonio detallando quien como y donde', verbose_name=b'Testimonios')),
                ('ministerio_ninos', models.TextField(help_text=b'Describa las \xc3\xbaltimas actividades con ni\xc3\xb1os en el \xc3\xbaltimo semestre como: campamentos, alcances evangelisticos, escuela b\xc3\xadblica, deportes,grupos de vida, etc.', verbose_name=b'Ministerio de los Ni\xc3\xb1os')),
                ('uso_local', models.TextField(help_text=b'Como se uso el local en el \xc3\xbaltimo semestre. ej.: Escuela de d\xc3\xada, entrenamiento vocacional, estudios b\xc3\xadblicos, ministerio de mujeres, proyecci\xc3\xb3n de pel\xc3\xadculas etc.', verbose_name=b'Uso del local de la iglesia')),
                ('fotos', models.FileField(help_text=b'Suba un un archivo comprimido en .rar o .zip de fotos que evidencien los programas realizados en el templo', upload_to=db.models.ruta_fotos_informe_publico, verbose_name=b'Fotos evidencia', validators=[db.models.validate_comprimidos])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'informes p\xfablicos',
            },
            bases=(models.Model,),
        ),
    ]
