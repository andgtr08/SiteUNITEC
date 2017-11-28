"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from django.contrib import admin
from django.contrib.auth.views import login, logout
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name="home"),
    url(r'^index/', index),
    url(r'^restrito/$', restrito, name='restrito'),
)
