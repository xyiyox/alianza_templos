import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alianza_templos.settings")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
