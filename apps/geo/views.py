from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.geo.models import Category, Point, PointCategory


class BaseView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class ListPoints(BaseView):

    def _filter(self, request, points):
        categories_filter = request.GET.get("categories")
        if categories_filter:
            categories_filter = categories_filter.split(",")
            points = points.filter(
                id__in=PointCategory.objects.filter(
                    category__id__in=categories_filter
                ).values_list("point_id")
            )
        return points

    def _get_points(self, request):
        points = Point.objects.values(
            "id", "longitude", "latitude", "address", "description"
        )
        points = self._filter(request, points)
        return points

    def get(self, request):
        points = self._get_points(request)
        return Response({"error": "not", "data": points})


class CategoryPoints(BaseView):

    def _get_categories(self):
        categories = Category.objects.values("id", "title", "transliteration")
        return categories

    def get(self, request):
        categories = self._get_categories()
        return Response({"error": "not", "data": categories})
