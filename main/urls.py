from django.conf.urls import url
from django.urls import path, re_path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('login',  views.hacer_login,  name='hacer_login'),
    path('logout', views.hacer_logout, name='hacer_logout'),
    
    path('home-nacional', views.home_nacional, name='home_nacional'),
    url(r'^home-nacional/etapa/(?P<etapa>\d+)/$', views.home_nacional, name='home_nacional_etapa'),
    url(r'^home-nacional/region/(?P<region>\d+)/$', views.home_nacional_region, name='home_nacional_region'),

    url(r'^home-otros/etapa/(?P<etapa>\d+)/$', views.home_otros, name='home_otros_etapa'),
    url(r'^home-otros/region/(?P<region>\d+)/$', views.home_otros_region, name='home_otros_region'),
    

    path('home-regional', views.home_regional, name='home_regional'),
    path('home-local',    views.home_local,    name='home_local'),
    path('home-otros',    views.home_otros,    name='home_otros'),
    
    path('proyecto/<int:pk>/', views.proyecto, name='proyecto'),
    path('proyecto/nuevo/', views.proyecto_nuevo, name='proyecto_new'),
    re_path(r'^proyecto/(?P<pk>\d+)/editar/(?P<form_index>[0-9]{1})/$', views.proyecto_edit, name='proyecto_edit'), #si necesitamos mas de dos digitos cambiar {1}
    url(r'^proyecto/(?P<pk>\d+)/zip/$', views.proyecto_zip, name='proyecto_zip'),
    url(r'^proyecto/(?P<pk>\d+)/pdf/$', views.proyecto_pdf, name='proyecto_pdf'), 
    url(r'^proyecto/(?P<pk>\d+)/done/$', views.done, name='done'),     

    url(r'^proyecto/(?P<pk>\d+)/informe/(?P<index>[0-9]{1})/$', views.informe_pdf, name='informe_pdf'), 

    url(r'^proyecto/(?P<pk>\d+)/autorizaciones/$', views.autorizaciones, name='autorizaciones'),
    url(r'^proyecto/(?P<pk>\d+)/asignaciones/$', views.asignaciones, name='asignaciones'),
    url(r'^proyecto/(?P<pk>\d+)/pin/$', views.asignar_pin, name='asignar_pin'),
    url(r'^proyecto/(?P<pk>\d+)/planos/$', views.planos, name='planos'),

    
    url(r'^proyecto/(?P<pk>\d+)/fotos/$', views.fotos, name='fotos'),
    url(r'^proyecto/(?P<pk>\d+)/evento/$', views.evento, name='evento'),
    url(r'^proyecto/(?P<pk>\d+)/dedicacion/$', views.dedicacion, name='dedicacion'),
    path('cron/alert/', views.alert, name='alert'),
    path('oauth2callback', views.auth_return, name='auth_return'),

    path('informe-semestral/publico/783w5g95h0795g94h84u50', views.informe_semestral_publico, name='informe_semestral_publico' ),
    path('informe-respuesta', views.informe_respuesta, name='informe_respuesta' ),
    path('informes-semestrales', views.informes_semestrales, name='informes_semestrales'),
    url(r'^informes-semestrales/(?P<pk>\d+)$', views.informe_semestral, name='informe_semestral'),
    url(r'^informes-semestrales/(?P<pk>\d+)/edit$', views.informe_semestral_edit, name='informe_semestral_edit'),
    url(r'^informes-semestrales/(?P<pk>\d+)/csv$', views.informe_semestral_csv, name='informe_semestral_csv'),


    path('mapa', views.mapa, name='mapa'),
    url(r'^mapa/(?P<filtro>\w+)/$', views.mapa, name='mapa_filtro'),
]

