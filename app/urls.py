from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('', include('artist.urls')),
    path('', include('gallery.urls')),
    path('', include('programs.urls')),
    path('', include('advertising.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
