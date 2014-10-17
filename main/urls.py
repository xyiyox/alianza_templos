from django.conf.urls import patterns, url

from main.views import Aplicacion
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('main.views',

    url(r'^$', 'home', name='home'),
    url(r'^home-local$', 'home_local', name='home_local'),
    url(r'^home-nacional$', 'home_nacional', name='home_nacional'),
    url(r'^login$', 'hacer_login', name='hacer_login'),
    url(r'^logout$', 'hacer_logout', name='hacer_logout'),
    
    url(r'^aplicacion/(?P<pk>\d+)/$', login_required(Aplicacion.as_view()), name='aplicacion_edit'),
    url(r'^aplicacion$', login_required(Aplicacion.as_view()), name='aplicacion'),
    url(r'^aplicacion/(?P<pk>\d+)/comentarios$', 'ver_comentarios', name='ver_comentarios')
)

