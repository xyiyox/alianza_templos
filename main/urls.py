from django.conf.urls import patterns, url

from main.views import Aplicacion
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('main.views',

    url(r'^$', 'home', name='home'),
    url(r'^login$', 'hacer_login', name='hacer_login'),
    url(r'^logout$', 'hacer_logout', name='hacer_logout'),
    url(r'^aplicacion$', login_required(Aplicacion.as_view()), name='aplicacion'),
)

