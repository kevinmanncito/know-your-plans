from settings.common import *

# Django settings for production

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'wsgi.production.application'

ALLOWED_HOSTS = [
    '.knowyourplans.com',
]

STATIC_ROOT = "/opt/know_your_plans/static/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'know_your_plans',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'kevin',
        'PASSWORD': 'know2014',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'APP_DSN_HERE',
}
