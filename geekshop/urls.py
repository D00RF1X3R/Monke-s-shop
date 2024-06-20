from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('catalog/', include('catalog.urls')),
    path('forum/', include('forum.urls')),
    path('business/', include('business.urls')),
    path('users/', include('users.urls')),
]
