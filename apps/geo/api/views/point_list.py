# thirdparty
from drf_yasg.utils import swagger_auto_schema

# django
from rest_framework.response import Response

# project
from apps.geo.api.swagger import point_manual_parameters
from apps.geo.api.views import BaseView
from apps.geo.models import Label, Point, PointCategory


class PointList(BaseView):
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
        points = Point.objects.values("id", "lng", "lat", "address", "description")
        points = self._filter(request, points)
        for point in points:
            point["id"] = str(point["id"])
            point["categories"] = [
                {
                    "id": point.id,
                    "title": point.title,
                    "transliteration": point.transliteration,
                }
                for point in Point.objects.get(id=point["id"]).categories
            ]
        return points

    @swagger_auto_schema(
        operation_summary="Get all points", manual_parameters=point_manual_parameters
    )
    def get(self, request):
        points = self._get_points(request)
        return Response({"error": "not", "data": points})
