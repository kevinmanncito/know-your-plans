from settings.common import *

# Django settings for production

DEBUG = False
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'wsgi.production.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'APP_DB_NAME',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'APP_DB_USER_NAME',
        'PASSWORD': 'SECURE_PASSWORD',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'APP_DSN_HERE',
}