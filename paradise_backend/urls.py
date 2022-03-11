from django.contrib import admin
from django.urls import path

from apps.geo.views import CategoryList, LabelList, ListPoints

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/points", ListPoints.as_view(), name="fractions"),
    path("api/categories", CategoryList.as_view(), name="categories"),
    path("api/labels", LabelList.as_view(), name="labels"),
]
