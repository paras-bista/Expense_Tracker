from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # <-- path and include come from here
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
]

if settings.DEBUG:  # only serve media in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
