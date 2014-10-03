"""
Django settings for fiddlr project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


# Automatically detect whether this is running on my development
# computer, otherwise assuming that the environment is production.
isProduction = False
try:
    open(os.path.join(BASE_DIR,'.dev'))
except IOError:
    isProduction = True

PRODUCTION = isProduction
DEBUG = not isProduction
TEMPLATE_DEBUG = DEBUG


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fwa',
    'djangobower',
    'rest_framework',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10,
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fiddlr.urls'

WSGI_APPLICATION = 'fiddlr.wsgi.application'


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config(),
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)


# django-bower
BOWER_COMPONENTS_ROOT = BASE_DIR

BOWER_INSTALLED_APPS = (
    'angular',
    'angular-bootstrap',
    'angular-filter',
    'angular-google-maps',
    'angular-typeahead',
    'angular-ui-bootstrap',
    'angulerjs',
    'bootstrap',
    'danialfarid-angular-file-upload',
    'galleria',
    'jquery',
    'less',
    'lodash',
    'modernizr',
    'ng-galleria',
    'normalize.css',
    'restangular',
    'typeahead.js',
    'underscore',
)


# API key used for Google Maps etc.
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
