# django
from django.conf.urls import include
from django.urls import path

# project
from apps.geo.api.api_urls import api_urls

urlpatterns = [
    path("api/", include(api_urls)),
]