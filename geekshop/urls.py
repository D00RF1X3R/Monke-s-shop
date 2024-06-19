from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("homepage.urls")),
    path('about/', include("about.urls")),
    path('catalog/', include("catalog.urls")),
    path('forum/', include("forum.urls")),
    path('business/', include("business.urls")),
    path('business/', include("django.contrib.auth.urls")),
    path('users/', include("users.urls")),
    path('users/', include("django.contrib.auth.urls")),
]
