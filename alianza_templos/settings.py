try:
    from . local_settings import *
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
    #'django.contrib.formtools',

    'crispy_forms',
    'session_security',
    'debug_toolbar',
    'map_field',
    'sorl.thumbnail',

    'usuarios',
    'main',
    'db',
)

MIDDLEWARE = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # para django session security
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
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

SECRET_KEY = '_=9hq-$t_uv1ckf&s!y2$9g$1dm*6p1cl%*!^mg=7gr)!zj32d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'

# Configuracion de la ruta para los archivos e imagenes
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
MEDIA_URL = '/media/'

################### configuraciones adicionales ####################

# configuarcion de email
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT

EMAIL_COMUNICACIONES = 'sandra.montanez@laalianzacristiana.co'
EMAIL_DEVELOPER = 'felipe.valencia@laalianzacristiana.co'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # para suit
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',

                'main.context_processors.notificaciones',
                'main.context_processors.etapa',
                'main.context_processors.region',
                'main.context_processors.civil',
                'main.context_processors.choices',
                'main.context_processors.fotos',
            ],
        },
    },
]




################### configuraciones de paquetes instalados ####################

SUIT_CONFIG = {
    'ADMIN_NAME': '<a href="/"><img width="150" height=40 src="/static/main/img/logo.png"></a>',
    'MENU_ICONS': {
        'usuarios': 'icon-user',
        'auth': 'icon-lock',
    },
    'CONFIRM_UNSAVED_CHANGES': True
}



# configuracion de crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# configuracion de django session security
#SESSION_SECURITY_WARN_AFTER = 30
#SESSION_SECURITY_EXPIRE_AFTER = 60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


LOGIN_URL = '/login'

TASK_UPLOAD_FILE_TYPES = ['rar', 'zip',]
TASK_UPLOAD_FILE_MAX_SIZE = "5242880"



