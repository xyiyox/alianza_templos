"""
Django settings for alianza_templos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

try:
    from local_settings import *
except ImportError:
    print('no se encuentra local_settings')
    pass 



AUTH_USER_MODEL = 'usuarios.Usuario'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = (
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',

    'crispy_forms',
    'session_security',
    'debug_toolbar',
    'map_field',

    'south',
    'usuarios',
    'main',
    'db',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_security.middleware.SessionSecurityMiddleware', # para django session security
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'alianza_templos.urls'

WSGI_APPLICATION = 'alianza_templos.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'

# Configuracion de la ruta para los archivos e imagenes

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
MEDIA_URL = '/media/'

################### configuraciones de paquetes instalados ####################


# configuracion de django suit
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'La Alianza',
    'MENU_ICONS': {
        'usuarios': 'icon-user',
        'auth': 'icon-lock',
    }
}

# configuracion de crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# configuracion de django session security
#SESSION_SECURITY_WARN_AFTER = 30
#SESSION_SECURITY_EXPIRE_AFTER = 60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


LOGIN_URL = '/login'
