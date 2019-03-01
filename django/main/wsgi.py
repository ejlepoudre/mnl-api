"""
<<<<<<< HEAD
WSGI config for main project.
=======
WSGI config for MNL project.
>>>>>>> upstream/master

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
>>>>>>> upstream/master
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

application = get_wsgi_application()
