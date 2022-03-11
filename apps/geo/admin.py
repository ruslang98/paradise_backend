from django.contrib import admin

from apps.geo.models import Category, Point, PointCategory

admin.site.register(Point)
admin.site.register(Category)
admin.site.register(PointCategory)
