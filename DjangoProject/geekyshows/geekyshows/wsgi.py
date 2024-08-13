"""
WSGI config for geekyshows project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os 

from django.core.wsgi import get_wsgi_application
#package-django.core, module-wsgi, function-get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geekyshows.settings')
# geekyshows.settings - value , define settings module to env variable
# os.environ - a mapping object representing the string env
# setdefault - function
# DJANGO_SETTINGS_MODULE - env variable
application = get_wsgi_application()
# application - object callable 
# get_wsgi_application() - function