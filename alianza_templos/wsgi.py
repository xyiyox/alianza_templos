import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alliance.settings")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#import newrelic.agent
#newrelic.agent.initialize(os.path.join(BASE_DIR, 'alliance/newrelic.ini'))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
