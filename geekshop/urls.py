from django.contrib import admin
from django.urls import include, path
from geekshop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('catalog/', include('catalog.urls')),
    path('forum/', include('forum.urls')),
    path('business/', include('business.urls')),
    path('business/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
