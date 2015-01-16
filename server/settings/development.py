import os

from settings.common import *

# Django settings for development.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = 'wsgi.development.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'know_your_plans',                          # Or path to database file if using sqlite3.
        'USER': 'kevin',
        'PASSWORD': 'know2014',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
