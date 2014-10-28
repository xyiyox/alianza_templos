from django.conf.urls import patterns, url

from main.views import Aplicacion
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('main.views',

    url(r'^$', 'home', name='home'),
    url(r'^login$',  'hacer_login',  name='hacer_login'),
    url(r'^logout$', 'hacer_logout', name='hacer_logout'),
    
    url(r'^home-nacional$', 'home_nacional', name='home_nacional'),
    url(r'^home-regional$', 'home_regional', name='home_regional'),
    url(r'^home-local$',    'home_local',    name='home_local'),
    
    url(r'^proyecto/(\d+)/$', 'proyecto', name='proyecto'),
    url(r'^proyecto/nuevo/$', login_required(Aplicacion.as_view()), name='proyecto_new'),
    url(r'^proyecto/(?P<pk>\d+)/editar/$', login_required(Aplicacion.as_view()), name='proyecto_edit'),
    
)

