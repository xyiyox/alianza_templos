"""
WSGI config for alianza_templos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alianza_templos.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
