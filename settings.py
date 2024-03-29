"""
Django settings for jobiewebsite project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os 
from dotenv import load_dotenv
from pathlib import Path  # python3 only
from corsheaders.defaults import default_headers

env_path = Path('/var/www/jobiewebsite/.env')
load_dotenv(dotenv_path=env_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'level': 'DEBUG'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': "debug.log",
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console', 'file']
        },
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
STATIC_URL = '/static/'
# SECURITY WARNING: don't run with debug turned on in production!
STATIC_ROOT = os.path.join(BASE_DIR, 'jobiewebsite/static/')
if os.getenv("SERVER") == "development":
    DEBUG = True
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = False
    ALLOWED_HOSTS = ["apiportfolio.jobiewinser.co.uk", "portfolio.jobiewinser.co.uk", "localhost"]
STATICFILES_DIRS = [
    '/var/www/jobiewebsite/staticfiles/'
]
    




# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'import_export',
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES_DIR = os.path.join(BASE_DIR,'jobiewebsite/templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#DATABASES = {
#   'default': {
 #       'ENGINE': 'django.db.backends.sqlite3',
 #       'NAME': BASE_DIR / 'db.sqlite3',
 #   }
#}

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':os.getenv("DBNAME"),
        'USER':os.getenv("DBUSER"),
        'PASSWORD':os.getenv("DBPASSWORD"),
        'HOST':'localhost',
        'PORT':'',
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'jobiewebsite/media')

MEDIA_URL = '/media/'

auth_classes = [
        "rest_framework.authentication.SessionAuthentication",
        "api.authentication.TokenAuthentication"               
    ]
    
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": auth_classes,
    
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticatedOrReadOnly",
        "rest_framework.permissions.AllowAny"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer', #DO NOT REMOVE, VIEWFLOW NEEDS THIS???
        'rest_framework.renderers.TemplateHTMLRenderer', #DO NOT REMOVE, VIEWFLOW NEEDS THIS???
    )
}

CORS_ALLOWED_ORIGINS = [
    'http://portfolio.jobiewinser.co.uk',
    # '82.37.38.164'
]
CSRF_TRUSTED_ORIGINS = ['http://portfolio.jobiewinser.co.uk']

CORS_REPLACE_HTTPS_REFERER = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    "Access-Control-Allow-Origin",
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jobiewinser@gmail.com'
EMAIL_HOST_PASSWORD = 'zcosfvgjmblebclj'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True