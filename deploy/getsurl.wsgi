import os, sys
sys.path.append('/var/www/shorturl')
os.environ['DJANGO_SETTINGS_MODULE'] = 'getsurl.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
