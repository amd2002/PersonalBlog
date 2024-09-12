import os
import sys

# Ajouter le chemin du projet à sys.path
path = '/home/massaid2002/blog'  # Assure-toi que ce chemin est correct
if path not in sys.path:
    sys.path.append(path)

# Définir la variable d'environnement pour le module de paramètres Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
