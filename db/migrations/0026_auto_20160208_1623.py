# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0025_edificacion_fecha_aprox_dedicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunidad',
            name='corregimiento',
            field=models.CharField(help_text=b'Ingrese el Corregimiento donde se va realizar la construccion, si aplica.', max_length=50, null=True, verbose_name=b'Corregimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comunidad',
            name='vereda',
            field=models.CharField(help_text=b'Ingrese el la Vereda donde se va realizar la construccion, si aplica.', max_length=50, null=True, verbose_name=b'Vereda', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='congregacion',
            name='celular_pastor',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Celular del pastor', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='congregacion',
            name='email_pastor',
            field=models.CharField(max_length=80, null=True, verbose_name=b'Email del pastor', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='congregacion',
            name='telefono_pastor',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Telefono del pastor', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='informacion_adicional',
            field=models.TextField(help_text=b'Ingrese informacion adicional sobre el tereno, como desniveles, tipo de lugar, datos adionales que permitan agilizar el proceso de la creacion de los planos.', null=True, verbose_name=b'Datos adicionales del Terreno', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='localidad_terreno',
            field=models.SmallIntegerField(default=0, verbose_name=b'Localidad del Terreno', choices=[(0, b'Rural'), (1, b'Urbano'), (2, b'Veredal')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='tipo_permiso',
            field=models.SmallIntegerField(default=0, verbose_name=b'Tipo de Permiso', choices=[(0, b'Curaduria'), (1, b'Planeacion'), (2, b'No')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='tipo_terreno',
            field=models.SmallIntegerField(default=0, verbose_name=b'Estado del Terreno', choices=[(0, b'Plano'), (1, b'Desnivel')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='ubucacion_construccion',
            field=models.SmallIntegerField(default=0, verbose_name=b'Ubicacion de la Construccion', choices=[(0, b'Esquina Derecha'), (1, b'Esquina Izquierda'), (2, b'En la Mitad')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='edificacion',
            name='vecinos_terreno',
            field=models.SmallIntegerField(default=0, verbose_name=b'Vecinos del Terreno', choices=[(0, b'Izquierda'), (1, b'Derecha'), (2, b'Atras'), (3, b'Der/Izq')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='escritura_terreno',
            field=models.FileField(help_text=b'Mostrando la prueba de propiedad', upload_to=db.models.calcular_ruta, verbose_name=b'Escritura del terreno Autenticada, o Promesa de Compra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='foto_construccion',
            field=models.ImageField(help_text=b'Mostrando claramente el terreno donde se va a construir la iglesia', upload_to=db.models.calcular_ruta, verbose_name=b'Foto del Terreno'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='manzana_catastral',
            field=models.FileField(help_text=b'Mostrando las dimensiones de la propiedad y la ubicaci\xc3\xb3n de la tierra, Si el instituto Augustin Codaci no le proporciona este documento, puede adjuntar un dibujo de la localizacion(mapa peque\xc3\xb1o) de el lugar donde se construira el templo', upload_to=db.models.calcular_ruta, verbose_name=b'Manzana Catastral o Croquis dibujado a Mano'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='permiso_construccion',
            field=models.FileField(help_text=b'Debe agregar el permiso de construccion, si no necesida debe agregar la prueba de que no necesita permiso.', upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Permiso de construcci\xc3\xb3n o Certificado de que no necesita Oermiso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='alcance',
            field=models.BooleanField(default=False, verbose_name=b'Somos llamados por la Gran Comisi\xc3\xb3n de Cristo para compartir de nuestra fe. Con la ayuda de Cristo, nos comprometemos a plantar al menos cinco (5) grupos de vida o campos misioneros durante los tres (3) primeros a\xc3\xb1os despu\xc3\xa9s/siguientes de la fecha de consagraci\xc3\xb3n del proyecto.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='discipulado',
            field=models.BooleanField(default=False, verbose_name=b'Estoy de acuerdo en discipular a los creyentes de la iglesia atravez de la EFI y el Seminario en virtud de un plan acordado por La Alianza, y seguir los pasos correspondientes y descritos en el Manual de Asociaci\xc3\xb3n de Crecimiento de la Iglesia.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='found_commitment',
            field=models.BooleanField(default=False, verbose_name=b'Estoy al dia con el 13%, y me comprometo a mantenerlo durante y despues de la construccion.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='terminacion',
            field=models.BooleanField(default=False, verbose_name=b'Nosotros, con la ayuda de Dios, terminaremos la construcci\xc3\xb3n del edificio en la fecha prevista en proyecto. La Alianza ha de ser notificada por el socio de cualquier cambio planeado en la fecha de Dedicacion.', choices=[(True, 'Yes'), (False, 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tiempo_limite',
            field=models.PositiveSmallIntegerField(help_text=b'Tiempo en que se terminar\xc3\xa1 la construcci\xc3\xb3n (Meses), Templo 6 Max Meses, Templo/Obra Max 8 Meses.', verbose_name=b'Tiempo Limite'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_construccion',
            field=models.SmallIntegerField(default=0, help_text=b'Seleccione el tipo de Construccion, Tenga encuenta para el caso de Templo/Obra Social de identificar como se va construir esta instalacion, esta informacion es importante y debe ser precisa', verbose_name=b'Tipo de Construcci\xc3\xb3n', choices=[(0, b'Templo'), (1, b'Obra Social'), (2, b'Templo/Obra Social (Arriba)'), (3, b'Templo/Obra Social (Lateral Izq)'), (4, b'Templo/Obra Social (Atras)'), (5, b'Templo/Obra Social (Lateral Der)')]),
            preserve_default=True,
        ),
    ]
