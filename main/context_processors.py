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