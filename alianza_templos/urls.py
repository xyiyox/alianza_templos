from django.conf.urls import include, url
from django.views import static

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'session_security/', include('session_security.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root':settings.MEDIA_ROOT,}),
]

