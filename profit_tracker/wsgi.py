"""
WSGI config for profit_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Use production settings if available
if os.environ.get('RAILWAY_ENVIRONMENT'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profit_tracker.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profit_tracker.settings')

application = get_wsgi_application()
