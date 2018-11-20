"""
WSGI config for learning_templates project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_templates.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_templates.settings")
>>>>>>> f91ae2aadf8e2a0f8ead3bb259711c1c109d277b

application = get_wsgi_application()
