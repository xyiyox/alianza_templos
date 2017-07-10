from django.conf.urls import patterns, url


urlpatterns = patterns('main.views',

    url(r'^$', 'home', name='home'),
    url(r'^login$',  'hacer_login',  name='hacer_login'),
    url(r'^logout$', 'hacer_logout', name='hacer_logout'),
    
    url(r'^home-nacional$', 'home_nacional', name='home_nacional'),
    url(r'^home-nacional/etapa/(?P<etapa>\d+)/$', 'home_nacional', name='home_nacional_etapa'),
    url(r'^home-nacional/region/(?P<region>\d+)/$', 'home_nacional_region', name='home_nacional_region'),

    url(r'^home-otros/etapa/(?P<etapa>\d+)/$', 'home_otros', name='home_otros_etapa'),
    url(r'^home-otros/region/(?P<region>\d+)/$', 'home_otros_region', name='home_otros_region'),
    

    url(r'^home-regional$', 'home_regional', name='home_regional'),
    url(r'^home-local$',    'home_local',    name='home_local'),
    url(r'^home-otros$',    'home_otros',    name='home_otros'),
    
    url(r'^proyecto/(\d+)/$', 'proyecto', name='proyecto'),
    url(r'^proyecto/nuevo/$', 'proyecto_nuevo', name='proyecto_new'),
    url(r'^proyecto/(?P<pk>\d+)/editar/(?P<form_index>[0-9]{1})/$', 'proyecto_edit', name='proyecto_edit'), #si necesitamos mas de dos digitos cambiar {1}
    url(r'^proyecto/(?P<pk>\d+)/zip/$', 'proyecto_zip', name='proyecto_zip'),
    url(r'^proyecto/(?P<pk>\d+)/pdf/$', 'proyecto_pdf', name='proyecto_pdf'), 
    url(r'^proyecto/(?P<pk>\d+)/done/$', 'done', name='done'),     

    url(r'^proyecto/(?P<pk>\d+)/informe/(?P<index>[0-9]{1})/$', 'informe_pdf', name='informe_pdf'), 

    url(r'^proyecto/(?P<pk>\d+)/autorizaciones/$', 'autorizaciones', name='autorizaciones'),
    url(r'^proyecto/(?P<pk>\d+)/asignaciones/$', 'asignaciones', name='asignaciones'),
    url(r'^proyecto/(?P<pk>\d+)/planos/$', 'planos', name='planos'),

    #url(r'^proyecto/(?P<pk>\d+)/informe/$', 'informe', name='informe'),
    
    url(r'^proyecto/(?P<pk>\d+)/fotos/$', 'fotos', name='fotos'),
    url(r'^proyecto/(?P<pk>\d+)/evento/$', 'evento', name='evento'),
    url(r'^proyecto/(?P<pk>\d+)/dedicacion/$', 'dedicacion', name='dedicacion'),
    url(r'^cron/alert/$', 'alert', name='alert'),
    url(r'^oauth2callback', 'auth_return', name='auth_return'),

    url(r'^informe-semestral/publico/783w5g95h0795g94h84u50$', 'informe_semestral_publico', name='informe_semestral_publico' ),
    url(r'^informe-respuesta$', 'informe_respuesta', name='informe_respuesta' ),
    url(r'^informes-semestrales$', 'informes_semestrales', name='informes_semestrales'),
    url(r'^informes-semestrales/(?P<pk>\d+)$', 'informe_semestral', name='informe_semestral'),
    #url(r'^informes-semestrales/(?P<pk>\d+)/editar$', 'informe_semestral', name='informe_semestral'),
)

