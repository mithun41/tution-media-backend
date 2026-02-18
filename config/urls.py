"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include # include import kora hoyeche
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Registration, Login (JWT) er jonno accounts app connect
    path('api/accounts/', include('accounts.urls')),
    
]

# Media files (profile_pics, library resources) access korar jonno
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)