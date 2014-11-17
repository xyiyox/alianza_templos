# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import db.models
from django.conf import settings
import map_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjuntos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto_construccion', models.ImageField(help_text=b'Mostrando claramente el \xc3\xa1rea donde se va a construir la iglesia', upload_to=db.models.calcular_ruta, verbose_name=b'Foto del sitio de construcci\xc3\xb3n')),
                ('foto_congregacion', models.ImageField(help_text=b'Mostrando el lugar donde se reunen actualmente', upload_to=db.models.calcular_ruta, verbose_name=b'Foto de la congregaci\xc3\xb3n')),
                ('foto_pastor', models.FileField(help_text=b'Incluya una foto del pastor en caso de no aparecer en la foto de la congregaci\xc3\xb3n', upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Foto del Pastor', blank=True)),
                ('permiso_construccion', models.FileField(help_text=b'Si se requiere, debe agregarlo', upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Permiso de construcci\xc3\xb3n', blank=True)),
                ('escritura_terreno', models.FileField(help_text=b'Mostrando la prueba de propiedad', upload_to=db.models.calcular_ruta, verbose_name=b'Escritura del terreno')),
                ('plan_terreno', models.FileField(help_text=b'Mostrando las dimensiones de la propiedad y la ubicaci\xc3\xb3n de la tierra', upload_to=db.models.calcular_ruta, verbose_name=b'Plan de Terreno')),
                ('plan_construccion', models.FileField(help_text=b'Obligatorio para todos los planes que no hacen parte de los aprobados por ICM', upload_to=db.models.calcular_ruta, null=True, verbose_name=b'Plan de construcci\xc3\xb3n', blank=True)),
                ('historia_congregacion', models.FileField(help_text=b'Incluya una breve historia de la congregaci\xc3\xb3n', upload_to=db.models.calcular_ruta, verbose_name=b'Historia de la congregaci\xc3\xb3n')),
                ('testimonio_pastor', models.FileField(help_text=b'Incluya el testimonio del pastor de la congregaci\xc3\xb3n', upload_to=db.models.calcular_ruta, verbose_name=b'Testimonio del pastor')),
            ],
            options={
                'verbose_name_plural': 'adjuntos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(verbose_name=b'Comentario')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comentario_padre', models.ForeignKey(blank=True, to='db.Comentario', null=True)),
                ('commenter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('poblacion_comunidad', models.CharField(max_length=40, verbose_name=b'Cantidad de poblaci\xc3\xb3n')),
                ('region', models.CharField(max_length=30, verbose_name=b'Departamento')),
                ('capital_depto', models.CharField(max_length=30, verbose_name=b'Capital del Departamento')),
                ('distancia_capital', models.PositiveSmallIntegerField(help_text=b'Por favor ingrese el valor en Kilometros (Km)', verbose_name=b'Distancia a la capital')),
            ],
            options={
                'verbose_name_plural': 'ciudades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Condiciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('construccion', models.BooleanField(default=False, verbose_name=b'Proveeremos fotos y reportes del progres de la construcci\xc3\xb3n con cada solicitud de pago y seguiremos los lineamientos \n\t\t\t\t\t\t\t\texplicados en el manual Church Growth Partnership.', choices=[(True, 'Yes'), (False, 'No')])),
                ('mantenimiento', models.BooleanField(default=False, verbose_name=b'Lorem ipsum Enim dolore nisi reprehenderit sunt ea non elit ad ex ad qui consequat esse.', choices=[(True, 'Yes'), (False, 'No')])),
                ('actividades', models.BooleanField(default=False, verbose_name=b'Lorem ipsum Duis do ut ut commodo anim nostrud dolor ex velit mollit in deserunt reprehenderit quis dolor nulla Ut \n\t\t\t\t\t\t\t\tlaborum Duis nulla laborum et dolor consectetur eiusmod adipisicing ea veniam.', choices=[(True, 'Yes'), (False, 'No')])),
                ('discipulado', models.BooleanField(default=False, verbose_name=b'Lorem ipsum Est in Ut id aliqua aliqua et deserunt sunt adipisicing.', choices=[(True, 'Yes'), (False, 'No')])),
                ('alcance', models.BooleanField(default=False, verbose_name=b'Lorem ipsum Adipisicing eu laboris dolore dolor deserunt adipisicing laborum mollit dolore exercitation occaecat \n\t\t\t\t\t\t\t\treprehenderit anim qui velit in.', choices=[(True, 'Yes'), (False, 'No')])),
                ('found_trust', models.BooleanField(default=False, verbose_name=b'We will accept funds from ICM as a trust from the Lord.', choices=[(True, 'Yes'), (False, 'No')])),
                ('found_commitment', models.BooleanField(default=False, verbose_name=b'We understand that we have our Church building because others have shared with us. As a way to give to others what \n\t\t\t\t\t\t\t\tothers have given to us, we will contribute to the Covenant Fund account maintained by our Church organization. \n\t\t\t\t\t\t\t\tOur commitment to do this is in realization of God\xe2\x80\x99s goodness to our Congregation and of the many Congregations still \n\t\t\t\t\t\t\t\twaiting for an opportunity to build. Our monthly contribution amount will be agreed upon by our Church organization \n\t\t\t\t\t\t\t\tand reviewed annually. The monthly contribution will be a reflection of how God has prospered our Church organization.', choices=[(True, 'Yes'), (False, 'No')])),
                ('found_payment', models.CharField(help_text=b'Cantidad o Porcentaje', max_length=20, verbose_name=b"Fund Payment: The monthly contribution to the Covenant Fund, will begin the month following the dedication of the \n\t\t\t\t\t\t\t\tbuilding. This contribution will be either a fixed amount each month or a fixed percentage of the congregation's monthly \n\t\t\t\t\t\t\t\tofferings")),
                ('presupuesto', models.BooleanField(default=False, verbose_name=b"We will, with God's help, complete the building of this project within the stated budget and we understand that any \n\t\t\t\t\t\t\t\tadditional costs must be covered by the congregation.", choices=[(True, 'Yes'), (False, 'No')])),
                ('terminacion', models.BooleanField(default=False, verbose_name=b'We will, with God\xe2\x80\x99s help, complete the building of this project on schedule. ICM is to be notified by the Partner of \n\t\t\t\t\t\t\t\tany changes to planned Dedication Date.', choices=[(True, 'Yes'), (False, 'No')])),
                ('comentarios', models.TextField(verbose_name=b'Comentarios adiccionanles (OPCIONAL) (Provea cualquier otra informaci\xc3\xb3n que ayudar\xc3\xa1 a ICM a procesar esta aplicaci\xc3\xb3n).', blank=True)),
                ('aceptacion', models.BooleanField(default=False, help_text=b'I acknowledge and agree to the terms and conditions outlined in the Church Growth Partnership Manual.')),
                ('nombre_completo', models.CharField(help_text=b'(Nombre de la persona autorizada a presentar esta aplicaci\xc3\xb3n.)', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'condiciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Congregacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fecha_fundacion', models.DateField(help_text=b'Dia/Mes/A\xc3\xb1o', verbose_name=b'Fecha de Fundaci\xc3\xb3n')),
                ('lengua_primaria', models.CharField(max_length=20, verbose_name=b'Lengua primaria hablada')),
                ('region', models.SmallIntegerField(help_text=b'La Regi\xc3\xb3n a la que pertenece la Iglesia', verbose_name=b'Regi\xc3\xb3n', choices=[(0, b'Central'), (1, b'Sur Oriental'), (2, b'Mecusab'), (3, b'Pac\xc3\xadfico'), (4, b'Sur'), (5, b'Valle')])),
                ('asistencia_general', models.SmallIntegerField(verbose_name=b'Asistencia general promedio')),
                ('asistencia_ninos', models.SmallIntegerField(verbose_name=b'Asistencia general promedio de ni\xc3\xb1os')),
                ('miembros_adultos', models.SmallIntegerField(help_text=b'Recuerde que se considera como miembro a aquel que ha sido bautizado', verbose_name=b'Cantidad de miembros adultos')),
                ('miembros_ninos', models.SmallIntegerField(verbose_name=b'Cantidad de miembros ni\xc3\xb1os')),
                ('ingreso_mensual', models.DecimalField(verbose_name=b'Ingreso mensual promedio', max_digits=15, decimal_places=3)),
                ('nombre_pastor', models.CharField(max_length=50, verbose_name=b'Nombre del pastor')),
                ('estado_civil', models.SmallIntegerField(verbose_name=b'Estado civil', choices=[(0, b'Soltero'), (1, b'Casado'), (2, b'Viudo'), (3, b'Otro')])),
                ('cant_hijos', models.PositiveSmallIntegerField(verbose_name=b'Cantidad de hijos')),
                ('entrenamiento_biblico', models.PositiveSmallIntegerField(verbose_name=b'A\xc3\xb1os de entrenamiento Biblico')),
                ('titulos_obtenidos', models.CharField(max_length=70, verbose_name=b'Titulos obtenidos')),
                ('anios_iglesia', models.PositiveSmallIntegerField(verbose_name=b'A\xc3\xb1os de servicio en la congregaci\xc3\xb3n actual')),
                ('anios_ministerio', models.PositiveSmallIntegerField(verbose_name=b'A\xc3\xb1os de servicio en el ministerio')),
                ('hay_material', models.BooleanField(default=False, verbose_name=b'\xc2\xbfEl pastor conoce el material del Instituto Biblico del Aire?')),
                ('q1_why_not', models.TextField(null=True, verbose_name=b'\xc2\xbfPor que no?', blank=True)),
                ('usa_material', models.BooleanField(default=False, verbose_name=b'\xc2\xbfEl pastor ha acordado usar este material para crecimiento de la iglesia?')),
                ('q2_why_not', models.TextField(null=True, verbose_name=b'\xc2\xbfPor que no?', blank=True)),
                ('q2_how_do', models.TextField(null=True, verbose_name=b'\xc2\xbfComo lo hace?', blank=True)),
            ],
            options={
                'verbose_name_plural': 'congregaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Edificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_proyecto', models.CharField(max_length=40, verbose_name=b'Nombre del Proyecto')),
                ('direccion', models.TextField(verbose_name=b'Direcci\xc3\xb3n')),
                ('coordenadas', map_field.fields.GeoLocationField(help_text=b'Navegue acercando el mapa con el bot\xc3\xb3n \n\t\t\t\t\t\t\t\t<button type="button" class="btn btn-default btn-xs" disabled><i class="fa fa-plus"></i></button> o doble click \n\t\t\t\t\t\t\t\ty arrastrando el mouse hasta el lugar mas exacto posible donde se realizar\xc3\xa1 el proyecto y ubique ahi el marcador.', max_length=100)),
                ('owner_lote', models.SmallIntegerField(verbose_name=b'Due\xc3\xb1o del Lote', choices=[(0, b'Alianza Cristiana'), (1, b'Otro')])),
                ('tipo_adquisicion', models.SmallIntegerField(verbose_name=b'M\xc3\xa9todo de Adquisici\xc3\xb3n', choices=[(0, b'Comprado'), (1, b'Donado')])),
                ('dimensiones_terreno', models.CharField(help_text=b'Ingrese Ancho x Largo en Metros', max_length=30, verbose_name=b'Dimensiones del Terreno')),
                ('dimensiones_edificio', models.CharField(help_text=b'Ingrese las medidas en Metros. Para construcci\xc3\xb3n de templos las m\xc3\xa9didas autorizadas son 200 mt cuadrados y para guarderias 150 mt cuadrados. Si las m\xc3\xa9didas superan estos valores entonces se asume que la congregaci\xc3\xb3n aporta el excedente del dinero', max_length=30, verbose_name=b'Dimensiones del Edificio')),
                ('num_pisos', models.SmallIntegerField(default=1, verbose_name=b'Cantidad de Pisos', choices=[(1, 1), (2, 2)])),
                ('tipo_construccion', models.SmallIntegerField(verbose_name=b'Tipo de Construcci\xc3\xb3n', choices=[(0, b'Iglesia'), (1, b'Guarderia'), (2, b'Iglesia/Guarderia')])),
                ('metodo_construccion', models.SmallIntegerField(verbose_name=b'M\xc3\xa9todo de Construcci\xc3\xb3n', choices=[(0, b'Nueva Edificacion'), (1, b'Otro')])),
                ('requiere_permiso', models.BooleanField(default=False, verbose_name=b'\xc2\xbfRequiere permiso de construcci\xc3\xb3n?')),
                ('tiempo_limite', models.PositiveSmallIntegerField(help_text=b'Tiempo en que se terminar\xc3\xa1 la construcci\xc3\xb3n (Meses)', verbose_name=b'Tiempo Limite')),
                ('estado', models.SmallIntegerField(choices=[(0, b'EdificacionForm'), (1, b'ComunidadForm'), (2, b'CongregacionForm'), (3, b'FuentesFinancierasForm'), (4, b'CondicionesForm'), (5, b'Terminado')])),
                ('etapa_actual', models.PositiveSmallIntegerField(choices=[(0, b'Diligenciamiento'), (1, b'Aprobaci\xc3\xb3n Regional'), (2, b'Asignaci\xc3\xb3n de Ingeniero/Arquitecto'), (3, b'Creaci\xc3\xb3n de Planos'), (4, b'Aprobaci\xc3\xb3n Ingeniero'), (5, b'Aprobaci\xc3\xb3n Tesorero'), (6, b'Aprobaci\xc3\xb3n Nacional'), (7, b'Aprobaci\xc3\xb3n Internacional'), (8, b'En Espera de Cupo'), (9, b'En Espera de Recursos'), (10, b'En Construcci\xc3\xb3n'), (11, b'Esperando Correcciones'), (12, b'Finalizaci\xc3\xb3n')])),
                ('aprobacion_regional', models.BooleanField(default=False, verbose_name=b'Dar aprobaci\xc3\xb3n Regional')),
                ('aprobacion_arquitecto', models.BooleanField(default=False, verbose_name=b'Dar aprobaci\xc3\xb3n de Arquitecto')),
                ('aprobacion_ingeniero', models.BooleanField(default=False, verbose_name=b'Dar aprobaci\xc3\xb3n de Ingeniero')),
                ('aprobacion_nacional', models.BooleanField(default=False, verbose_name=b'Dar aprobaci\xc3\xb3n Nacional')),
                ('arquitecto', models.ForeignKey(related_name='arquitecto', verbose_name=b'Arquitecto Asignado', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('ingeniero', models.ForeignKey(related_name='ingeniero', verbose_name=b'Ingeniero Asignado', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('usuario', models.ForeignKey(related_name='usuario', verbose_name=b'Responsable', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'edificaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FuentesFinanciacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('valor', models.DecimalField(verbose_name=b'Valor', max_digits=15, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InformacionFinanciera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mano_obra', models.PositiveIntegerField(default=0, verbose_name=b'Costo de la Mano de obra', blank=True)),
                ('valor_materiales', models.PositiveIntegerField(default=0, verbose_name=b'Costo de Materiales de construcci\xc3\xb3n', blank=True)),
                ('dinero_efectivo', models.PositiveIntegerField(help_text=b'Ingrese el valor en Dolares (Estados Unidos). <br>Puede usar <a href="http://www.colombia.com/cambio_moneda/" target="_blank">este enlace</a> como convertidor de moneda.', verbose_name=b'Dinero Ahorrado')),
                ('valor_terreno', models.PositiveIntegerField(help_text=b'Ingrese el valor en Dolares (Estados Unidos)', verbose_name=b'Valor del Terreno')),
                ('valor_solicitado', models.PositiveIntegerField(help_text=b'Recuerde que este dinero esta expresado en Dolares (Estados Unidos)', verbose_name=b'Dinero Solicitado', choices=[(0, 14000), (1, 25000), (2, 39000)])),
                ('num_voluntarios', models.PositiveSmallIntegerField(help_text=b'\xc2\xbfCuantas personas tiene disponibles para ayudar fisicamente en la construcci\xc3\xb3n?', verbose_name=b'Cantidad de Voluntarios')),
                ('desc_voluntarios', models.TextField(help_text=b'Describa que trabajos pueden hacer los Voluntarios y cuantas horas semanales pueden donar', verbose_name=b'Descripci\xc3\xb3n')),
                ('dias_donados', models.PositiveSmallIntegerField(help_text=b'\xc2\xbfCuantos dias de trabajo donaran aquellos que no pueden ayudar fisicamente a la obra?', null=True, verbose_name=b'Dias Donados', blank=True)),
                ('costo_total', models.PositiveIntegerField(help_text=b'Ingrese el valor en Dolares (Estados Unidos)', verbose_name=b'Costo total del proyecto')),
                ('edificacion', models.OneToOneField(to='db.Edificacion')),
            ],
            options={
                'verbose_name_plural': 'informaciones financieras',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fuentesfinanciacion',
            name='info_financiera',
            field=models.ForeignKey(to='db.InformacionFinanciera'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='congregacion',
            name='edificacion',
            field=models.OneToOneField(to='db.Edificacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='condiciones',
            name='edificacion',
            field=models.ForeignKey(to='db.Edificacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comunidad',
            name='edificacion',
            field=models.OneToOneField(to='db.Edificacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='edificacion',
            field=models.ForeignKey(to='db.Edificacion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='edificacion',
            field=models.ForeignKey(to='db.Edificacion'),
            preserve_default=True,
        ),
    ]
