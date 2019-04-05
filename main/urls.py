from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views as views


urlpatterns = [
    path('', views.main, name='main')
    path('display_tab', views.display_tab, name='display')
]
