from db.models import Etapa, Edificacion,Congregacion
from usuarios.models import Usuario

def etapa(request):
	return {'list_etapas': Etapa.ETAPA_ACTUAL}

def region(request):
	return {'list_regions': Congregacion.REGION_CHOICES}	

def civil(request):
	return {'list_civil': Congregacion.ESTADO_CIVIL_CHOICES}	

def choices(request):
	BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
	return {'list_status':BOOL_CHOICES}		

def fotos(request):	
	#Arreglo de requerimientos de fotos segun la etapa

	   #    CONS_P1 = 11 # FIJA
	   #	CONS_P2 = 12 # FIJA
	   #	CONS_P3 = 13  # SOLO TEMPLO OBRA/SOCIAL
	   #	
	   #	DEDICACION = 14 #FIJA

	  # (0, 'Templo',),
	  # (1, 'Obra Social'),
	  #	(2, 'Templo/Obra Social (Arriba)'),
	  #	(3, 'Templo/Obra Social (Lateral)'),
	  #	(4, 'Templo/Obra Social (Atras)'),

	OBRA_SOCIAL_P1 = """ Fotos nivel ventanas, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""
	OBRA_SOCIAL_P2 = """ Fotos nivel viga de amarre y techo, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""

	# VERIFICAR SI SI CAMBIO PARA TEMPLO
	TEMPLO_P1 = """ Fotos nivel ventanas, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""
	TEMPLO_P2 = """ Fotos nivel viga de amarre y techo, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""

	# OBRA SOCIAL/TEMPLO CON SEGUNDO PISO
	OBRTMP_A_P1 = """ Fotos 4 paredes primer piso y plancha del 2do piso , Esto implica. 1 Foto para(Frente, lateral, atras, adentro)  """
	OBRTMP_A_P2 = """ Fotos Anteriores y 2do piso paredes, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""
	OBRTMP_A_P3 = """ Fotos Anteriores y Techo, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""

	# OBRA SOCIAL/TEMPLO LATERAL
	OBRTMP_B_P1 = """ Fotos nivel ventanas, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""
	OBRTMP_B_P2 = """ Fotos nivel viga de amarre y techo, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""
	OBRTMP_B_P3 = """ Fotos nivel viga de amarre y techo, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""

	# OBRA SOCIAL/TEMPLO ATRAS
	OBRTMP_C_P1 = """ Fotos nivel ventanas, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""
	OBRTMP_C_P2 = """ Fotos nivel viga de amarre y techo, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""
	OBRTMP_C_P3 = """ Fotos nivel viga de amarre y techo, Esto implica. 1 Foto para(Frente, lateral, atras, adentro)"""

	#LA DEDICACION ES IGUAL PARA TODOS
	DEDICACION = """ Fotos de la Dedicacion, Pintura, Ventanas, Color, Todo Organizado 1 Foto para (Frente, lateral, atras, adentro)"""

	LISTADO = (
			(0, ((11, TEMPLO_P1), (12,TEMPLO_P2) )),	
			(1, ((11, OBRA_SOCIAL_P1), (12,OBRA_SOCIAL_P2) )),	
			(2, ((11, OBRTMP_A_P1), (12,OBRTMP_A_P2), (13,OBRTMP_A_P3) )),	
			(3, ((11, OBRTMP_B_P1), (12,OBRTMP_B_P2), (13,OBRTMP_B_P3) )),		
			(4, ((11, OBRTMP_C_P1), (12,OBRTMP_C_P2), (13,OBRTMP_C_P3) )),	
		)	
	LISTADO = (
			 ((11, TEMPLO_P1), (12,TEMPLO_P2) ),	
			 ((11, OBRA_SOCIAL_P1), (12,OBRA_SOCIAL_P2) ),	
			 ((11, OBRTMP_A_P1), (12,OBRTMP_A_P2), (13,OBRTMP_A_P3) ),	
			 ((11, OBRTMP_B_P1), (12,OBRTMP_B_P2), (13,OBRTMP_B_P3) ),		
			 ((11, OBRTMP_C_P1), (12,OBRTMP_C_P2), (13,OBRTMP_C_P3) ),	
		)

	LISTADO = {
		'CAD_011': TEMPLO_P1,
		'CAD_012': TEMPLO_P2,
		'CAD_014': DEDICACION,
		
		'CAD_111': OBRA_SOCIAL_P1,
		'CAD_112': OBRA_SOCIAL_P2,
		'CAD_114': DEDICACION,

		'CAD_211': OBRTMP_A_P1,
		'CAD_212': OBRTMP_A_P2,
		'CAD_213': OBRTMP_A_P3,
		'CAD_214': DEDICACION,

		'CAD_311': OBRTMP_B_P1,
		'CAD_312': OBRTMP_B_P2,
		'CAD_313': OBRTMP_B_P3,
		'CAD_314': DEDICACION,

		'CAD_411': OBRTMP_C_P1,
		'CAD_412': OBRTMP_C_P2,
		'CAD_413': OBRTMP_C_P3,
		'CAD_414': DEDICACION
	}

	return {'list_fotos':LISTADO}		

def notificaciones(request):
	etapas = {}
	if request.user.is_authenticated():
		if request.user.tipo == Usuario.NACIONAL:
			etapas = Etapa.objects.filter().order_by('-created', '-pk')[:20]
		elif request.user.tipo == Usuario.REGIONAL:
			pass
		elif request.user.tipo == Usuario.ARQUITECTO:
			pass
		elif request.user.tipo == Usuario.INGENIERO:
			pass
		elif request.user.tipo == Usuario.TESORERO:
			pass
		elif request.user.tipo == Usuario.LOCAL:
			edificaciones_user = Edificacion.objects.filter(usuario=request.user)
			etapas = []
			for e in edificaciones_user:
				etapas += e.etapa_set.all()[:20]
			etapas = sorted(etapas, key=lambda etapa: -etapa.pk)
	return {'etapas': etapas}