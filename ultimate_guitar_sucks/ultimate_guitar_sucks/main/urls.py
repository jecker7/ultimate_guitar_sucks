from django.conf.urls import include, url
from django.contrib import admin
from django.cof.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    url('r^$', views.main, name='main')
] + static(settings.STATIC_URL,  document_root = settings.STATIC_ROOT
           + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

