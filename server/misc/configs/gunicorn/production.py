SITE = 'know_your_plans'

command = '/opt/{0}/bin/gunicorn'.format(SITE)
pythonpath = '/opt/{0}/{0}/server'.format(SITE)
bind = '127.0.0.1:8000'

preload_app = True
workers = 6
