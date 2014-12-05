from settings.common import *

# Django settings for staging

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'wsgi.staging.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'APP_DB_NAME',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'APP_DB_USER_NAME',
        'PASSWORD': 'SECURE_PW_HERE',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
