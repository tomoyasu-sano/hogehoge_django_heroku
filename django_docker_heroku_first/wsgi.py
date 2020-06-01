"""
WSGI config for django_docker_heroku_first project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

"""
import os

from django.core.wsgi import get_wsgi_application

import sys
print(sys.path.append(os.path.dirname(os.path.abspath(__file__))))
print("--------------")

#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_docker_heroku_first.settings")

application = get_wsgi_application()
"""

import os

#from django.core.wsgi import get_wsgi_application
path = "/Users/tomoyasu.sano/dev/Training/deploy/django-docker-first/django_docker_heroku_first"

from django.core.wsgi import get_wsgi_application
import sys
print(sys.path.append(os.path.dirname(os.path.abspath(path))))
print("--------------")


#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_docker_heroku_first.settings")

#django-docker-first
#django_docker_heroku_first
#application = get_wsgi_application()
