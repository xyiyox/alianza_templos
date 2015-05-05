# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20150428_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='aprobacion_internacional',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='actividades',
            field=models.BooleanField(default=False, verbose_name=b'Por un periodo de tres (3) a\xc3\xb1os, despu\xc3\xa9s de que el proyecto es dedicado, proporcionaremos seis (6) informes del crecimiento y las actividades del proyecto seg\xc3\xban lo dispuesto en el Manual de Asociaci\xc3\xb3n de Crecimiento de la Iglesia. Estos seis (6) informes de actividades ser\xc3\xa1n entregadas cada seis (6) meses (calendario vigente) en enero y julio.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='alcance',
            field=models.BooleanField(default=False, verbose_name=b'Somos llamados por la Gran Comisi\xc3\xb3n de Cristo para compartir de nuestra fe. Con la ayuda de Cristo, nos comprometemos a plantar al menos cinco (5) iglesias hermanas durante los tres (3) primeros a\xc3\xb1os despu\xc3\xa9s/siguientes de la fecha de consagraci\xc3\xb3n del proyecto.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='construccion',
            field=models.BooleanField(default=False, verbose_name=b'Proporcionare fotos/imagines e informes del progreso de la construcci\xc3\xb3n con cada solicitud de pago y seguir\xc3\xa9 las instrucciones como se explica en el Manual de Asociaci\xc3\xb3n de Iglesia en Crecimiento.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='discipulado',
            field=models.BooleanField(default=False, verbose_name=b'Estoy de acuerdo en nutrir a los creyentes en la iglesia en virtud de un plana cordado por ICM, y seguir los pasos correspondientes y descritos en el Manual de Asociaci\xc3\xb3n de Crecimiento de la Iglesia.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='found_commitment',
            field=models.BooleanField(default=False, verbose_name=b'Compromiso de la Inversi\xc3\xb3n:\xc2\xa0Entendemos que tenemos el edificio de la iglesia debido a que otros nos han ayudado. Como una manera de dar a los dem\xc3\xa1s de lo que otros nos han dado, vamos a contribuir a la cuenta de Pacto de Inversi\xc3\xb3n (13%) que se tiene por la organizaci\xc3\xb3n de nuestra Iglesia. El compromiso de hacer esto es ver la realizaci\xc3\xb3n de la bondad de Dios en nuestra congregaci\xc3\xb3n y de las muchas congregaciones que siguen en la espera de una oportunidad para construir.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='found_trust',
            field=models.BooleanField(default=False, verbose_name=b'Fondo/inversi\xc3\xb3n Trust:\xc2\xa0Acepto los fondos de ICM en reverencia y confianza al Se\xc3\xb1or Jes\xc3\xbas.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='mantenimiento',
            field=models.BooleanField(default=False, verbose_name=b'El edificio y los jardines se deben mantener bien de forma que atestig\xc3\xbcen la grandeza de Dios a la comunidad y como se explica en el Manual de Asociaci\xc3\xb3n de Crecimiento de la Iglesia.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='presupuesto',
            field=models.BooleanField(default=False, verbose_name=b'Nosotros, con la ayuda de Dios, terminaremos la construcci\xc3\xb3n del edificio estipulada en el presupuesto establecido en el proyecto y entendemos que los costos adicionales deben ser cubiertos por la congregaci\xc3\xb3n.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='terminacion',
            field=models.BooleanField(default=False, verbose_name=b'Nosotros, con la ayuda de Dios, terminaremos la construcci\xc3\xb3n del edificio en la fecha prevista en proyecto. ICM ha de ser notificada por el socio de cualquier cambio planeado en la fecha de Dedicacion.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='etapa_actual',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Arquitecto/Director de Obra/Tesorero'), (4, 'Creaci\xf3n de Planos'), (5, 'Aprobaci\xf3n Director de Obra'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_construccion',
            field=models.SmallIntegerField(default=0, verbose_name=b'Tipo de Construcci\xc3\xb3n', choices=[(0, b'Templo'), (1, b'Obra Social'), (2, b'Templo/Obra Social')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(max_length=2, choices=[(1, 'Diligenciamiento'), (2, 'Aprobaci\xf3n Regional'), (3, 'Asignaci\xf3n de Arquitecto/Director de Obra/Tesorero'), (4, 'Creaci\xf3n de Planos'), (5, 'Aprobaci\xf3n Director de Obra'), (6, 'Aprobaci\xf3n Tesorero'), (7, 'Aprobaci\xf3n Nacional'), (8, 'Aprobaci\xf3n Internacional'), (10, 'En Espera de Recursos')]),
            preserve_default=True,
        ),
    ]
