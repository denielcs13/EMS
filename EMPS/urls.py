
from django.conf.urls import include, url
from django.contrib import admin

import Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin phase
    url(r'^admin/', include(admin.site.urls)),

    #Login module
    url(r'^home/', include('Login.urls' , namespace='Login')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)