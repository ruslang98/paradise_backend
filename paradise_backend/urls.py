from django.contrib import admin
from django.urls import path

from apps.geo.views import CategoryPoints, ListPoints

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/points", ListPoints.as_view(), name="fractions"),
    path("api/categories", CategoryPoints.as_view(), name="categories"),
]
