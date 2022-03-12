from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.geo.models import Category, Label, Point, PointCategory


class BaseView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class ListPoints(BaseView):
    def _filter(self, request, points):
        categories_filter = request.GET.get("categories")
        labels_filter = request.GET.get("labels")
        limit_filter = request.GET.get("limit")
        if categories_filter:
            categories_filter = categories_filter.split(",")
            points = points.filter(
                id__in=PointCategory.objects.filter(
                    category__id__in=categories_filter
                ).values_list("point_id")
            )

        if labels_filter:
            categories = Label.objects.filter(id__in=labels_filter).values_list(
                "category_id"
            )
            points = points.filter(
                id__in=PointCategory.objects.filter(
                    category__id__in=categories
                ).values_list("point_id")
            )
        if limit_filter:
            try:
                limit_filter = int(limit_filter)
            except ValueError:
                return points
            points = points[:limit_filter]

        return points

    def _get_points(self, request):
        points = Point.objects.values(
            "id", "lng", "lat", "address", "description"
        )
        points = self._filter(request, points)
        for point in points:
            point['id'] = str(point['id'])
        return points

    def get(self, request):
        points = self._get_points(request)
        return Response({"error": "not", "data": points})


class CategoryList(BaseView):
    def _get_categories(self):
        categories = Category.objects.values("id", "title", "transliteration")
        return categories

    def get(self, request):
        categories = self._get_categories()
        return Response({"error": "not", "data": categories})


class LabelList(BaseView):
    def _filters(self, request, labels):
        category_filters = request.GET.get("categories")
        if category_filters:
            labels = labels.filter(category_id=category_filters)
        return labels

    def _get_lables(self, request):
        lables = Label.objects.values("id", "title", "category_id")
        lables = self._filters(request, lables)
        return lables

    def get(self, request):
        labels = self._get_lables(request)
        return Response({"error": "not", "data": labels})
