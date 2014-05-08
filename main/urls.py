from django.conf.urls import patterns, url



urlpatterns = patterns('main.views',

    url(r'^$', 'home', name='home'),
    url(r'^login$', 'hacer_login', name='hacer_login'),
    url(r'^logout$', 'hacer_logout', name='hacer_logout'),

)

