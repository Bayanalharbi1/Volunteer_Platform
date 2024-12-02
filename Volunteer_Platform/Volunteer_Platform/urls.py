from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),            # Main app
    path('volunteers/', include('volunteers.urls')),  # Volunteers app
    path('organization/', include('organization.urls')),  # Organization app
    path('auth/', include('django.contrib.auth.urls')),  # Authentication views
]

if settings.DEBUG:  # For serving media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
