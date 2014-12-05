"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/Users/kevin/Documents/Projects/know_your_plans_code/know_your_plans')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.development")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
