from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Tes autres URL patterns ici...
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('users/', include('users.urls')), 
     path('accounts/', include('django.contrib.auth.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
