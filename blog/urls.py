from django.contrib import admin
from django.urls import path, include
from articles import views as article_views  # Importer les vues des articles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_views.list_article, name='home'),  # La racine redirige vers list_article
    path('articles/', include('articles.urls')),  # Inclure les URLs de l'application articles
    path('users/', include('users.urls')),  # Inclure les URLs de l'application users (si existante)
]
