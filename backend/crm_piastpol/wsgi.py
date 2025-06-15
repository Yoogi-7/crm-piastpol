# crm_piastpol/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_piastpol.settings')

application = get_wsgi_application()
