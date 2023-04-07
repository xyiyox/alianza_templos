# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import db.models
from django.conf import settings
import map_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0066_auto_20200213_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjuntos',
            name='certificacion',
            field=models.FileField(verbose_name='Certificación', upload_to=db.models.calcular_ruta, help_text='Agregue certificación bancaria o de materiales'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='dedicacion',
            field=models.FileField(verbose_name='Dedicacion Comprimido', null=True, upload_to=db.models.calcular_ruta),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='escritura_terreno',
            field=models.FileField(verbose_name='Escritura del terreno Autenticada, o Promesa de Compra', upload_to=db.models.calcular_ruta, help_text='Mostrando la prueba de propiedad'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='foto_congregacion',
            field=models.ImageField(verbose_name='Foto de la congregación', upload_to=db.models.calcular_ruta, help_text='Mostrando el lugar donde se reunen actualmente'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='foto_construccion',
            field=models.ImageField(verbose_name='Foto del Terreno', upload_to=db.models.calcular_ruta, help_text='Mostrando claramente el terreno donde se va a construir la iglesia, jpg o png, minimo 600 x 480 pixeles, Tamaño maximo 2MB'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='foto_pastor',
            field=models.FileField(verbose_name='Foto del Pastor', upload_to=db.models.calcular_ruta, help_text='Incluya una foto del pastor en caso de no aparecer en la foto de la congregación'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='fotos_p1',
            field=models.FileField(verbose_name='Comprimido de Fotos', null=True, upload_to=db.models.calcular_ruta),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='fotos_p2',
            field=models.FileField(verbose_name='Comprimido de Fotos', null=True, upload_to=db.models.calcular_ruta),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='fotos_p3',
            field=models.FileField(verbose_name='Comprimido de Fotos', null=True, upload_to=db.models.calcular_ruta),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='historia_congregacion',
            field=models.FileField(verbose_name='Historia de la congregación', upload_to=db.models.calcular_ruta, help_text='Incluya una breve historia de la congregación preferiblemente en formato WORD.'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='manzana_catastral',
            field=models.FileField(verbose_name='Manzana Catastral o Croquis dibujado a Mano', upload_to=db.models.calcular_ruta, help_text='Mostrando las dimensiones de la propiedad y la ubicación de la tierra, Si el instituto Augustin Codaci no le proporciona este documento, puede adjuntar un dibujo de la localizacion(mapa pequeño) de el lugar donde se construira el templo'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='permiso_construccion',
            field=models.FileField(blank=True, null=True, upload_to=db.models.calcular_ruta, verbose_name='Permiso de construcción o Certificado de que no necesita Permiso', help_text='Debe agregar el permiso de construccion, si no necesida debe agregar la prueba de que no necesita permiso.'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='plan_construccion',
            field=models.FileField(blank=True, null=True, upload_to=db.models.calcular_ruta, verbose_name='Plan de construcción', help_text='Obligatorio para todos los planes que no hacen parte de los aprobados por ICM'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='planos_arquitecto',
            field=models.FileField(verbose_name='Planos', null=True, upload_to=db.models.calcular_ruta),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='planos_ingeniero',
            field=models.FileField(verbose_name='Planos', null=True, upload_to=db.models.calcular_ruta),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='testimonio_pastor',
            field=models.FileField(verbose_name='Testimonio del pastor', upload_to=db.models.calcular_ruta, help_text='Incluya el testimonio del pastor de la congregación preferiblemente en formato WORD.'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='descripcion',
            field=models.TextField(verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='capital_depto',
            field=models.CharField(choices=[('Arauca', 'Arauca'), ('Armenia', 'Armenia'), ('Barranquilla', 'Barranquilla'), ('Bogota', 'Bogotá'), ('Bucaramanga', 'Bucaramanga'), ('Cali', 'Cali'), ('Cartagena', 'Cartagena'), ('Cucuta', 'Cúcuta'), ('Florencia', 'Florencia'), ('Ibague', 'Ibagué'), ('Leticia', 'Leticia'), ('Manizales', 'Manizales'), ('Medellin', 'Medellín'), ('Mitu', 'Mitú'), ('Monteria', 'Montería'), ('Mocoa', 'Mocoa'), ('Neiva', 'Neiva'), ('Pasto', 'Pasto'), ('Pereira', 'Pereira'), ('Popayan', 'Popayán'), ('Puerto Carreno', 'Puerto Carreño'), ('Puerto Inirida', 'Puerto Inírida'), ('Quibdo', 'Quibdó'), ('Riohacha', 'Riohacha'), ('San Jose del Guaviare', 'San José del Guaviare'), ('Santa Marta', 'Santa Marta'), ('San Andres', 'San Andres'), ('Sincelejo', 'Sincelejo'), ('Tunja', 'Tunja'), ('Valledupar', 'Valledupar'), ('Villavicencio', 'Villavicencio'), ('Yopal', 'Yopal')], max_length=30, verbose_name='Capital del Departamento'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='corregimiento',
            field=models.CharField(blank=True, null=True, max_length=50, verbose_name='Corregimiento', help_text='Ingrese el Corregimiento donde se va realizar la construccion, si aplica.'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='distancia_capital',
            field=models.PositiveSmallIntegerField(verbose_name='Distancia del Proyecto a la capital', help_text='Por favor ingrese el valor en Kilometros (Km)'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='distancia_iglesia',
            field=models.PositiveSmallIntegerField(verbose_name='Distancia a la Iglesia', help_text='La iglesia más cercana debe estar minimo a 10 o 15 km. (ingrese valor en kilómetros)'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='iglesia_cercana',
            field=models.CharField(verbose_name='Iglesia más cercana', max_length=50, help_text='Iglesia más cercana al proyecto.'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='nombre',
            field=models.CharField(verbose_name='Nombre', max_length=50),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='poblacion_comunidad',
            field=models.CharField(verbose_name='Población', max_length=40, help_text='Cantidad de habitantes en número'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='region',
            field=models.CharField(choices=[('Amazonas', 'Amazonas'), ('Antioquia', 'Antioquia'), ('Arauca', 'Arauca'), ('Atlantico', 'Atlántico'), ('Bolivar', 'Bolívar'), ('Boyaca', 'Boyacá'), ('Caldas', 'Caldas'), ('Caqueta', 'Caquetá'), ('Casanare', 'Casanare'), ('Cauca', 'Cauca'), ('Cesar', 'Cesar'), ('Choco', 'Chocó'), ('Cundinamarca', 'Cundinamarca'), ('Cordoba', 'Córdoba'), ('Guainia', 'Guainía'), ('Guaviare', 'Guaviare'), ('Huila', 'Huila'), ('La Guajira', 'La Guajira'), ('Magdalena', 'Magdalena'), ('Meta', 'Meta'), ('Narino', 'Nariño'), ('Norte de Santander', 'Norte de Santander'), ('Putumayo', 'Putumayo'), ('Quindio', 'Quindío'), ('Risaralda', 'Risaralda'), ('San Andres', 'San Andrés'), ('Santander', 'Santander'), ('Sucre', 'Sucre'), ('Tolima', 'Tolima'), ('Valle del Cauca', 'Valle del Cauca'), ('Vaupes', 'Vaupés'), ('Vichada', 'Vichada')], max_length=30, verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='comunidad',
            name='vereda',
            field=models.CharField(blank=True, null=True, max_length=50, verbose_name='Vereda', help_text='Ingrese el la Vereda donde se va realizar la construccion, si aplica.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='aceptacion',
            field=models.BooleanField(validators=[db.models.validate_terminos], default=False, verbose_name='He leído y estoy de acuerdo con los Términos y Condiciones', help_text='Al aceptar usted reconoce que es responsable de la información suministrada en cada uno de los pasos anteriores\n\t\t\t\t\t\t\t\ty se compromete el cumplimiento de las condiciones aqui expuestas.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='actividades',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Por un periodo de tres (3) años, después de que el proyecto es dedicado, proporcionaremos seis (6) informes del crecimiento y las actividades del proyecto según lo dispuesto en el Manual de Asociación de Crecimiento de la Iglesia. Estos seis (6) informes de actividades serán entregadas cada seis (6) meses (calendario vigente) en enero y julio.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='alcance',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Somos llamados por la Gran Comisión de Cristo para compartir de nuestra fe. Con la ayuda de Cristo, nos comprometemos a plantar al menos cinco (5) grupos de vida o campos misioneros durante los tres (3) primeros años después/siguientes de la fecha de consagración del proyecto.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='comentarios',
            field=models.TextField(blank=True, verbose_name='Comentarios adiccionanles (OPCIONAL) (Provea cualquier otra información que ayudará a ICM a procesar esta aplicación).'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='construccion',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Proporcionaré fotos/imagenes e informes del progreso de la construcción con cada solicitud de pago y seguiré las instrucciones como se explica en el Manual de Asociación de Iglesia en Crecimiento.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='discipulado',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Estoy de acuerdo en discipular a los creyentes de la iglesia atravez de la EFI y el Seminario en virtud de un plan acordado por La Alianza, y seguir los pasos correspondientes y descritos en el Manual de Asociación de Crecimiento de la Iglesia.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='found_commitment',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Estoy al dia con el 13%, y me comprometo a mantenerlo durante y despues de la construccion.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='mantenimiento',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='El edificio y los jardines deben mantener bien de forma que atestigüen la grandeza de Dios a la comunidad, como se explica en el Manual de Asociación de Crecimiento de la Iglesia.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='nombre_completo',
            field=models.CharField(max_length=50, help_text='(Nombre de la persona autorizada a presentar esta aplicación.)'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='presupuesto',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Nosotros, con la ayuda de Dios, terminaremos la construcción del edificio estipulada en el presupuesto establecido en el proyecto y entendemos que los costos adicionales deben ser cubiertos por la congregación.'),
        ),
        migrations.AlterField(
            model_name='condiciones',
            name='terminacion',
            field=models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')], verbose_name='Nosotros, con la ayuda de Dios, terminaremos la construcción del edificio en la fecha prevista en proyecto. La Alianza ha de ser notificada por el socio de cualquier cambio planeado en la fecha de Dedicacion.'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='anios_iglesia',
            field=models.PositiveSmallIntegerField(verbose_name='Años de servicio en la congregación actual'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='anios_ministerio',
            field=models.PositiveSmallIntegerField(verbose_name='Años de servicio en el ministerio'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='asistencia_general',
            field=models.SmallIntegerField(verbose_name='Asistencia general promedio', help_text='Incluya adultos y niños.'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='asistencia_ninos',
            field=models.SmallIntegerField(verbose_name='Asistencia general promedio de niños'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='cant_hijos',
            field=models.PositiveSmallIntegerField(verbose_name='Cantidad de hijos'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='celular_pastor',
            field=models.CharField(verbose_name='Celular del pastor', max_length=20, help_text='Si no tiene celular, ponga un número de contacto.'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='email_pastor',
            field=models.CharField(verbose_name='Email del pastor', max_length=80, help_text='Crear correo electrónico nuevo o poner el mismo de esta cuenta.'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='entrenamiento_biblico',
            field=models.PositiveSmallIntegerField(verbose_name='Años de entrenamiento Biblico'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='estado_civil',
            field=models.SmallIntegerField(choices=[(0, 'Soltero'), (1, 'Casado'), (2, 'Viudo'), (3, 'Otro')], default=0, verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='fecha_fundacion',
            field=models.DateField(verbose_name='Fecha de Fundación de la Congregacion'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='ingreso_mensual',
            field=models.DecimalField(max_digits=15, verbose_name='Ingreso mensual promedio', decimal_places=3),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='lengua_primaria',
            field=models.CharField(verbose_name='Lengua Materna', max_length=20),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='miembros_adultos',
            field=models.SmallIntegerField(verbose_name='Cantidad de miembros adultos', help_text='Recuerde que se considera como miembro a aquel que ha sido bautizado'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='miembros_ninos',
            field=models.SmallIntegerField(verbose_name='Cantidad de miembros niños'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='nombre_pastor',
            field=models.CharField(verbose_name='Nombre del pastor', max_length=50),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='region',
            field=models.SmallIntegerField(choices=[(0, 'Central'), (1, 'Sur Oriental'), (2, 'Mecusab'), (3, 'Pacífico'), (4, 'Sur'), (5, 'Valle'), (6, 'Guámbianos'), (7, 'Paez'), (8, 'Bautista')], default=0, verbose_name='Región', help_text='La Región a la que pertenece la Iglesia'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='telefono_pastor',
            field=models.CharField(blank=True, null=True, max_length=20, verbose_name='Telefono del pastor'),
        ),
        migrations.AlterField(
            model_name='congregacion',
            name='titulos_obtenidos',
            field=models.CharField(verbose_name='Titulos obtenidos', max_length=50),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='arquitecto',
            field=models.ForeignKey(related_name='arquitecto', to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Arquitecto Asignado', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='coordenadas',
            field=map_field.fields.GeoLocationField(max_length=100, help_text='Navegue acercando el mapa con el botón \n\t\t\t\t\t\t\t\t<button type="button" class="btn btn-default btn-xs" disabled><i class="fa fa-plus"></i></button> o doble click \n\t\t\t\t\t\t\t\ty arrastrando el mouse hasta el lugar mas exacto posible donde se realizará el proyecto y ubique ahi el marcador.'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='dimensiones_edificio',
            field=models.CharField(verbose_name='Dimensiones del Edificio', max_length=30, help_text='Ingrese las medidas en Metros. Para construcción de templos las médidas autorizadas son 200 mt cuadrados y para obra social 150 mt cuadrados. Si las médidas superan estos valores entonces se asume que la congregación aporta el excedente del dinero'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='dimensiones_terreno',
            field=models.CharField(verbose_name='Dimensiones del Terreno', max_length=30, help_text='Ingrese Ancho x Largo en Metros'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='direccion',
            field=models.TextField(verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='estado',
            field=models.SmallIntegerField(choices=[(0, 'EdificacionForm'), (1, 'ComunidadForm'), (2, 'CongregacionForm'), (3, 'FuentesFinancierasForm'), (4, 'CondicionesForm'), (5, 'Terminado')]),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='icm_pin',
            field=models.CharField(blank=True, null=True, max_length=40, verbose_name='Pin de ICM'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='informacion_adicional',
            field=models.TextField(blank=True, null=True, verbose_name='Datos adicionales del Terreno', help_text='Ingrese informacion adicional sobre el tereno, como desniveles, tipo de lugar, datos adionales que permitan agilizar el proceso de la creacion de los planos.'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='ingeniero',
            field=models.ForeignKey(related_name='ingeniero', to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Maestro de Obra Asignado', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='localidad_terreno',
            field=models.SmallIntegerField(choices=[(0, 'Rural'), (1, 'Urbano'), (2, 'Veredal')], default=0, verbose_name='Localidad del Terreno'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='nombre_proyecto',
            field=models.CharField(verbose_name='Nombre del Proyecto', max_length=40),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='num_pisos',
            field=models.SmallIntegerField(choices=[(1, 1), (2, 2)], default=1, verbose_name='Cantidad de Pisos'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='owner_lote',
            field=models.SmallIntegerField(choices=[(0, 'Propio Iglesia Local'), (1, 'Otro')], default=0, verbose_name='Dueño del Lote'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='requiere_permiso',
            field=models.BooleanField(default=True, choices=[(True, 'Si'), (False, 'No')], verbose_name='¿Requiere permiso de construcción?'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tesorero',
            field=models.ForeignKey(related_name='tesorero', to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Tesorero Asignado', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tiempo_limite',
            field=models.PositiveSmallIntegerField(verbose_name='Tiempo Limite', help_text='Tiempo en que se terminará la construcción (Meses), Templo 6 Max Meses, Templo/Obra Max 8 Meses.'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_adquisicion',
            field=models.SmallIntegerField(choices=[(0, 'Comprado'), (1, 'Donado')], default=0, verbose_name='Método de Adquisición'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_construccion',
            field=models.SmallIntegerField(choices=[(0, 'Templo'), (1, 'Obra Social'), (2, 'Templo/Obra Social (Arriba)'), (3, 'Templo/Obra Social (Lateral Izq)'), (4, 'Templo/Obra Social (Atras)'), (5, 'Templo/Obra Social (Lateral Der)')], default=0, verbose_name='Tipo de Construcción', help_text='Seleccione el tipo de Construccion, Tenga encuenta para el caso de Templo/Obra Social de identificar como se va construir esta instalacion, esta informacion es importante y debe ser precisa'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_permiso',
            field=models.SmallIntegerField(choices=[(0, 'Curaduria'), (1, 'Planeacion'), (2, 'No')], default=0, verbose_name='Tipo de Permiso'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='tipo_terreno',
            field=models.SmallIntegerField(choices=[(0, 'Plano'), (1, 'Desnivel')], default=0, verbose_name='Estado del Terreno'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='ubucacion_construccion',
            field=models.SmallIntegerField(choices=[(0, 'Esquina Derecha'), (1, 'Esquina Izquierda'), (2, 'En la Mitad')], default=0, verbose_name='Ubicacion de la Construccion'),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='usuario',
            field=models.ForeignKey(related_name='usuario', to=settings.AUTH_USER_MODEL, verbose_name='Responsable', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='edificacion',
            name='vecinos_terreno',
            field=models.SmallIntegerField(choices=[(0, 'Izquierda'), (1, 'Derecha'), (2, 'Atras'), (3, 'Der/Izq')], default=0, verbose_name='Vecinos del Terreno'),
        ),
        migrations.AlterField(
            model_name='etapa',
            name='etapa',
            field=models.IntegerField(choices=[(1, 'Diligenciamiento'), (2, 'Aprobación Regional'), (3, 'Asignación de Usuarios'), (4, 'Creación de Planos'), (6, 'Aprobación Tesorero'), (7, 'Aprobación Nacional'), (8, 'Aprobación Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion'), (15, 'Informes Semestrales')]),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='banco',
            field=models.CharField(verbose_name='Nombre del Banco', default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='costo_total',
            field=models.PositiveIntegerField(verbose_name='Costo total del proyecto', help_text='Ingrese el valor en Pesos Colombianos (COP)'),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='desc_voluntarios',
            field=models.TextField(verbose_name='Descripción', help_text='Describa que trabajos pueden hacer los Voluntarios y cuantas horas semanales pueden donar'),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='dinero_efectivo',
            field=models.PositiveIntegerField(verbose_name='Dinero Ahorrado', help_text='Ingrese el valor en Pesos Colombianos (COP), El total con el que cuenta Fisicamente'),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='num_voluntarios',
            field=models.PositiveSmallIntegerField(verbose_name='Cantidad de Voluntarios', help_text='¿Cuantas personas tiene disponibles para ayudar fisicamente en la construcción?'),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='numero_cuenta',
            field=models.CharField(verbose_name='Numero de Cuenta', default='00-00000-00', max_length=40, help_text='Ingrese el Numero de Cuenta,(Necesario si se aprueba el proyecto para hacer las consignaciones)'),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='tipo_cuenta',
            field=models.SmallIntegerField(choices=[(0, 'Ahorros'), (1, 'Corriente')], default=0, verbose_name='Tipo de Cuenta'),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='titular_cuenta',
            field=models.CharField(verbose_name='Titular', default='', max_length=100, help_text='Debe ser una cuenta de la iglesia'),
        ),
        migrations.AlterField(
            model_name='informacionfinanciera',
            name='valor_terreno',
            field=models.PositiveIntegerField(verbose_name='Valor del Terreno', help_text='Ingrese el valor en Pesos Colombianos (COP)'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='asistencia_general',
            field=models.PositiveIntegerField(verbose_name='Total Asistencia General', help_text='Servicios dominicales y grupos de vida incluyendo niños y no bautizados'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='asistencia_grupos',
            field=models.PositiveIntegerField(verbose_name='Asistencia grupos de vida', help_text='Asistencia promedio (por grupo no general) a los grupos de vida'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='bautismos_nuevos',
            field=models.PositiveIntegerField(verbose_name='Total Bautismos'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='conversiones',
            field=models.PositiveIntegerField(verbose_name='Conversiones', help_text='Total de personas que aceptaron a Cristo como su Señor y Salvador en el último semestre'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='fotos',
            field=models.FileField(validators=[db.models.validate_comprimidos], verbose_name='Fotos evidencia', upload_to=db.models.ruta_fotos_informe_semestral, help_text='Suba un un archivo comprimido en .rar o .zip de fotos que evidencien los programas realizados en el templo'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='grupos_vida',
            field=models.PositiveIntegerField(verbose_name='Grupos de vida o Celulas', help_text='Número actual de grupos de vida, grupos evangelísticos, casas de oración, grupos pequeños en casas etc..'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='miembros_actuales',
            field=models.PositiveIntegerField(verbose_name='Miembros Actuales', help_text='Bautizados'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='ministerio_ninos',
            field=models.TextField(verbose_name='Ministerio de los Niños', help_text='Describa las últimas actividades con niños en el último semestre como: campamentos, alcances evangelisticos, escuela bíblica, deportes,grupos de vida, etc.'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='no_bautismos',
            field=models.TextField(blank=True, null=True, verbose_name='Si no hubo bautismos', help_text='Explique por que no hubo bautismos'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='nuevos_miembros',
            field=models.PositiveIntegerField(verbose_name='Total Miembros Nuevos', help_text='Total de miembros agregados a la membresía de la iglesia en los últimos 6 meses'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='ofrendas',
            field=models.PositiveIntegerField(verbose_name='Ofrendas y Diezmos', help_text='Total dinero recaudado en ofrendas y diezmos en el último semestre'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='peticiones_oracion',
            field=models.TextField(verbose_name='Peticiones de Oracion', help_text='Especificas, accion de gracias o preocupaciones, favor explicar o dar detalles de la petición'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion',
            field=models.PositiveIntegerField(verbose_name='Plantacion de Iglesias', help_text='Cuantos grupos de vida, proyectos misioneros y/o iglesias fueron plantadas en el último semestre'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_fecha_1',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_fecha_2',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_fecha_3',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_lugar_1',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_lugar_2',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_lugar_3',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_nombre_1',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_nombre_2',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='plantacion_nombre_3',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='testimonios',
            field=models.TextField(verbose_name='Testimonios', help_text='liberaciones, conversiones, milagros, etc. Favor relatar brevemente el testimonio detallando quien como y donde'),
        ),
        migrations.AlterField(
            model_name='informesemestral',
            name='uso_local',
            field=models.TextField(verbose_name='Uso del local de la iglesia', help_text='Como se uso el local en el último semestre. ej.: Escuela de día, entrenamiento vocacional, estudios bíblicos, ministerio de mujeres, proyección de películas etc.'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='asistencia_general',
            field=models.PositiveIntegerField(verbose_name='Total Asistencia General', help_text='Servicios dominicales y grupos de vida incluyendo niños y no bautizados'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='asistencia_grupos',
            field=models.PositiveIntegerField(verbose_name='Asistencia grupos de vida', help_text='Asistencia promedio (por grupo no general) a los grupos de vida'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='bautismos_nuevos',
            field=models.PositiveIntegerField(verbose_name='Total Bautismos', help_text='Total de personas bautizadas en el último semestre'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='conversiones',
            field=models.PositiveIntegerField(verbose_name='Conversiones', help_text='Total de personas que aceptaron a Cristo como su Señor y Salvador en el último semestre'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='depto',
            field=models.CharField(choices=[('Amazonas', 'Amazonas'), ('Antioquia', 'Antioquia'), ('Arauca', 'Arauca'), ('Atlantico', 'Atlántico'), ('Bolivar', 'Bolívar'), ('Boyaca', 'Boyacá'), ('Caldas', 'Caldas'), ('Caqueta', 'Caquetá'), ('Casanare', 'Casanare'), ('Cauca', 'Cauca'), ('Cesar', 'Cesar'), ('Choco', 'Chocó'), ('Cundinamarca', 'Cundinamarca'), ('Cordoba', 'Córdoba'), ('Guainia', 'Guainía'), ('Guaviare', 'Guaviare'), ('Huila', 'Huila'), ('La Guajira', 'La Guajira'), ('Magdalena', 'Magdalena'), ('Meta', 'Meta'), ('Narino', 'Nariño'), ('Norte de Santander', 'Norte de Santander'), ('Putumayo', 'Putumayo'), ('Quindio', 'Quindío'), ('Risaralda', 'Risaralda'), ('San Andres', 'San Andrés'), ('Santander', 'Santander'), ('Sucre', 'Sucre'), ('Tolima', 'Tolima'), ('Valle del Cauca', 'Valle del Cauca'), ('Vaupes', 'Vaupés'), ('Vichada', 'Vichada')], max_length=30, verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='direccion',
            field=models.TextField(verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='fotos',
            field=models.FileField(validators=[db.models.validate_comprimidos], verbose_name='Fotos evidencia', upload_to=db.models.ruta_fotos_informe_publico, help_text='Suba un un archivo comprimido en .rar o .zip de fotos que evidencien los programas realizados en el templo'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='grupos_vida',
            field=models.PositiveIntegerField(verbose_name='Grupos de vida o Células', help_text='Número actual de grupos de vida, grupos evangelísticos, casas de oración, grupos pequeños en casas etc..'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='miembros_actuales',
            field=models.PositiveIntegerField(verbose_name='Miembros Actuales', help_text='Bautizados'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='ministerio_ninos',
            field=models.TextField(verbose_name='Ministerio de los Niños', help_text='Describa las últimas actividades con niños en el último semestre como: campamentos, alcances evangelisticos, escuela bíblica, deportes,grupos de vida, etc.'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='no_bautismos',
            field=models.TextField(blank=True, null=True, verbose_name='Si no hubo bautismos', help_text='Explique por que no hubo bautismos'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='nombre_proyecto',
            field=models.CharField(verbose_name='Nombre', max_length=40),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='nuevos_miembros',
            field=models.PositiveIntegerField(verbose_name='Total Miembros Nuevos', help_text='Total de miembros agregados a la membresía de la iglesia en los últimos 6 meses'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='ofrendas',
            field=models.PositiveIntegerField(verbose_name='Ofrendas y Diezmos', help_text='Total dinero recaudado en ofrendas y diezmos en el último semestre'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='persona',
            field=models.CharField(verbose_name='Encargado', max_length=40),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='peticiones_oracion',
            field=models.TextField(verbose_name='Peticiones de Oracion', help_text='Especificas, accion de gracias o preocupaciones, favor explicar o dar detalles de la petición'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_fecha_1',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_fecha_2',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_fecha_3',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_lugar_1',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_lugar_2',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_lugar_3',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_nombre_1',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_nombre_2',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='plantacion_nombre_3',
            field=models.CharField(verbose_name='', max_length=30),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='region',
            field=models.SmallIntegerField(choices=[(0, 'Central'), (1, 'Sur Oriental'), (2, 'Mecusab'), (3, 'Pacífico'), (4, 'Sur'), (5, 'Valle'), (6, 'Guanbianos'), (7, 'Paez'), (8, 'Bautista')], verbose_name='Región', help_text='La Región a la que pertenece la Iglesia'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='telefono',
            field=models.CharField(verbose_name='Teléfono', max_length=40, help_text='Celular y/o teléfono, puede poner ambos separados por coma'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='testimonios',
            field=models.TextField(verbose_name='Testimonios', help_text='liberaciones, conversiones, milagros, etc. Favor relatar brevemente el testimonio detallando quien como y donde'),
        ),
        migrations.AlterField(
            model_name='informesemestralpublico',
            name='uso_local',
            field=models.TextField(verbose_name='Uso del local de la iglesia', help_text='Como se uso el local en el último semestre. ej.: Escuela de día, entrenamiento vocacional, estudios bíblicos, ministerio de mujeres, proyección de películas etc.'),
        ),
        migrations.AlterField(
            model_name='plazo',
            name='etapa',
            field=models.PositiveSmallIntegerField(unique=True, choices=[(1, 'Diligenciamiento'), (2, 'Aprobación Regional'), (3, 'Asignación de Usuarios'), (4, 'Creación de Planos'), (6, 'Aprobación Tesorero'), (7, 'Aprobación Nacional'), (8, 'Aprobación Internacional'), (10, 'En Espera de Recursos'), (11, 'Primera Fase de Construccion'), (12, 'Segunda Fase de Construccion'), (13, 'Tercera Fase de Construccion'), (14, 'Dedicacion'), (15, 'Informes Semestrales')]),
        ),
        migrations.AlterField(
            model_name='plazo',
            name='peso',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='plazo',
            name='plazo',
            field=models.PositiveSmallIntegerField(help_text='plazo en días'),
        ),
    ]
