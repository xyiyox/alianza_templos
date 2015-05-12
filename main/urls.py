from django.conf.urls import patterns, url

from main.views import Aplicacion
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('main.views',

    url(r'^$', 'home', name='home'),
    url(r'^login$',  'hacer_login',  name='hacer_login'),
    url(r'^logout$', 'hacer_logout', name='hacer_logout'),
    
    url(r'^home-nacional$', 'home_nacional', name='home_nacional'),
    url(r'^home-nacional/etapa/(?P<etapa>\d+)/$', 'home_nacional', name='home_nacional_etapa'),
    url(r'^home-nacional/region/(?P<region>\d+)/$', 'home_nacional_region', name='home_nacional_region'),
    

    url(r'^home-regional$', 'home_regional', name='home_regional'),
    url(r'^home-local$',    'home_local',    name='home_local'),
    url(r'^home-otros$',    'home_otros',    name='home_otros'),
    
    url(r'^proyecto/(\d+)/$', 'proyecto', name='proyecto'),
    url(r'^proyecto/nuevo/$', login_required(Aplicacion.as_view()), name='proyecto_new'),
    url(r'^proyecto/(?P<pk>\d+)/editar/$', login_required(Aplicacion.as_view()), name='proyecto_edit'),
    url(r'^proyecto/(?P<pk>\d+)/editar/(?P<redireccion>[1-1]{1})/$', login_required(Aplicacion.as_view()), name='proyecto_edit_redirect'),  # esta url la usamos cuando redireccionamos de crecion a edit
    url(r'^proyecto/(?P<pk>\d+)/done/$', 'done', name='done'), 
    url(r'^proyecto/(?P<pk>\d+)/autorizaciones/$', 'autorizaciones', name='autorizaciones'),
    url(r'^proyecto/(?P<pk>\d+)/asignaciones/$', 'asignaciones', name='asignaciones')  
)

