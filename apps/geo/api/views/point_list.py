from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from apps.geo.api.serializers import PointSerializer
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
        points = Point.objects.all()
        points = self._filter(request, points)
        return points

    @swagger_auto_schema(
        operation_summary="Get all points", manual_parameters=point_manual_parameters
    )
    def get(self, request):
        points = self._get_points(request)
        serializer = PointSerializer(points, many=True)
        return Response({"error": "not", "data": serializer.data})

    def post(self, request):
        categories = request.data.get("categories")
        if categories:
            del request.data["categories"]

        validate_data = PointSerializer(request.data)
        new_point = Point.objects.create(**validate_data.data)

        if categories:
            for category in categories:
                PointCategory.objects.create(category_id=category, point=new_point)

        new_point_serializer = PointSerializer(new_point)
        return Response({"error": "not", "data": new_point_serializer.data})

