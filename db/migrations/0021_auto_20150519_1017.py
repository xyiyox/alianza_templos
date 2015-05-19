# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0020_auto_20150515_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidad',
            name='capital_depto',
            field=models.CharField(max_length=30, verbose_name=b'Capital del Departamento', choices=[(b'Arauca', b'Arauca'), (b'Armenia', b'Armenia'), (b'Barranquilla', b'Barranquilla'), (b'Bogota', b'Bogot\xc3\xa1'), (b'Bucaramanga', b'Bucaramanga'), (b'Cali', b'Cali'), (b'Cartagena', b'Cartagena'), (b'Cucuta', b'C\xc3\xbacuta'), (b'Florencia', b'Florencia'), (b'Ibague', b'Ibagu\xc3\xa9'), (b'Leticia', b'Leticia'), (b'Manizales', b'Manizales'), (b'Medellin', b'Medell\xc3\xadn'), (b'Mitu', b'Mit\xc3\xba'), (b'Monteria', b'Monter\xc3\xada'), (b'Mocoa', b'Mocoa'), (b'Neiva', b'Neiva'), (b'Pasto', b'Pasto'), (b'Pereira', b'Pereira'), (b'Popayan', b'Popay\xc3\xa1n'), (b'Puerto Carreno', b'Puerto Carre\xc3\xb1o'), (b'Puerto Inirida', b'Puerto In\xc3\xadrida'), (b'Quibdo', b'Quibd\xc3\xb3'), (b'Riohacha', b'Riohacha'), (b'San Jose del Guaviare', b'San Jos\xc3\xa9 del Guaviare'), (b'Santa Marta', b'Santa Marta'), (b'San Andres', b'San Andres'), (b'Sincelejo', b'Sincelejo'), (b'Tunja', b'Tunja'), (b'Valledupar', b'Valledupar'), (b'Villavicencio', b'Villavicencio'), (b'Yopal', b'Yopal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='region',
            field=models.CharField(max_length=30, verbose_name=b'Departamento', choices=[(b'Amazonas', b'Amazonas'), (b'Antioquia', b'Antioquia'), (b'Arauca', b'Arauca'), (b'Atlantico', b'Atl\xc3\xa1ntico'), (b'Bolivar', b'Bol\xc3\xadvar'), (b'Boyaca', b'Boyac\xc3\xa1'), (b'Caldas', b'Caldas'), (b'Caqueta', b'Caquet\xc3\xa1'), (b'Casanare', b'Casanare'), (b'Cauca', b'Cauca'), (b'Cesar', b'Cesar'), (b'Choco', b'Choc\xc3\xb3'), (b'Cundinamarca', b'Cundinamarca'), (b'Cordoba', b'C\xc3\xb3rdoba'), (b'Guainia', b'Guain\xc3\xada'), (b'Guaviare', b'Guaviare'), (b'Huila', b'Huila'), (b'La Guajira', b'La Guajira'), (b'Magdalena', b'Magdalena'), (b'Meta', b'Meta'), (b'Narino', b'Nari\xc3\xb1o'), (b'Norte de Santander', b'Norte de Santander'), (b'Putumayo', b'Putumayo'), (b'Quindio', b'Quind\xc3\xado'), (b'Risaralda', b'Risaralda'), (b'San Andres', b'San Andr\xc3\xa9s'), (b'Santander', b'Santander'), (b'Sucre', b'Sucre'), (b'Tolima', b'Tolima'), (b'Valle del Cauca', b'Valle del Cauca'), (b'Vaupes', b'Vaup\xc3\xa9s'), (b'Vichada', b'Vichada')]),
            preserve_default=True,
        ),
    ]
