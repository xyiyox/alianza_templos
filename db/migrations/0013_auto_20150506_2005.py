# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0012_auto_20150505_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuentesfinanciacion',
            name='info_financiera',
        ),
        migrations.DeleteModel(
            name='FuentesFinanciacion',
        ),
        migrations.RemoveField(
            model_name='informacionfinanciera',
            name='mano_obra',
        ),
        migrations.RemoveField(
            model_name='informacionfinanciera',
            name='valor_materiales',
        ),
        migrations.AddField(
            model_name='informacionfinanciera',
            name='numero_cuenta',
            field=models.CharField(default=b'00-00000-00', help_text=b'Ingrese el Numero de Cuenta,(Necesario si se aprueba el proyecto para hacer las consignaciones)', max_length=40, verbose_name=b'Numero de Cuenta'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='foto_pastor',
            field=models.FileField(help_text=b'Incluya una foto del pastor en caso de no aparecer en la foto de la congregaci\xc3\xb3n', upload_to=db.models.calcular_ruta, verbose_name=b'Foto del Pastor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='manzana_catastral',
            field=models.FileField(help_text=b'Mostrando las dimensiones de la propiedad y la ubicaci\xc3\xb3n de la tierra, Si el instituto Augustin Codaci no le proporciona este documento, puede adjuntar un dibujo de la localizacion(mapa peque\xc3\xb1o) de el lugar donde se construira el templo', upload_to=db.models.calcular_ruta, verbose_name=b'Manzana Catastral'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='alcance',
            field=models.BooleanField(default=False, verbose_name=b'Somos llamados por la Gran Comisi\xc3\xb3n de Cristo para compartir de nuestra fe. Con la ayuda de Cristo, nos comprometemos a plantar al menos cinco (5) grupos de vida durante los tres (3) primeros a\xc3\xb1os despu\xc3\xa9s/siguientes de la fecha de consagraci\xc3\xb3n del proyecto.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='construccion',
            field=models.BooleanField(default=False, verbose_name=b'Proporcionar\xc3\xa9 fotos/imagenes e informes del progreso de la construcci\xc3\xb3n con cada solicitud de pago y seguir\xc3\xa9 las instrucciones como se explica en el Manual de Asociaci\xc3\xb3n de Iglesia en Crecimiento.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='discipulado',
            field=models.BooleanField(default=False, verbose_name=b'Estoy de acuerdo en nutrir a los creyentes de la iglesia en virtud de un plan cordado por ICM, y seguir los pasos correspondientes y descritos en el Manual de Asociaci\xc3\xb3n de Crecimiento de la Iglesia.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='found_commitment',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfEsta al dia con el 13%?', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='mantenimiento',
            field=models.BooleanField(default=False, verbose_name=b'El edificio y los jardines deben mantener bien de forma que atestig\xc3\xbcen la grandeza de Dios a la comunidad, como se explica en el Manual de Asociaci\xc3\xb3n de Crecimiento de la Iglesia.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
    ]
