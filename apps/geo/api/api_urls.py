# django
from django.urls import path

# project
from apps.geo.api.views import (
    CategoryList,
    LabelList,
    PointList,
)

api_urls = [
    path("points/", PointList.as_view(), name="points"),
    path("categories/", CategoryList.as_view(), name="categories"),
    path("labels/", LabelList.as_view(), name="labels"),
]
