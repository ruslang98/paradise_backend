# thirdparty
from drf_yasg.utils import swagger_auto_schema

# django
from rest_framework.response import Response

# project
from apps.geo.api.swagger import label_manual_parameters
from apps.geo.api.views import BaseView
from apps.geo.models import Label


class LabelList(BaseView):
    def _filters(self, request, labels):
        category_filters = request.GET.get("categories")
        if category_filters:
            labels = labels.filter(category_id=category_filters)
        return labels

    def _get_lables(self, request):
        labels = Label.objects.values("id", "title", "category_id")
        labels = self._filters(request, labels)
        return labels

    @swagger_auto_schema(
        operation_summary="Get all labels", manual_parameters=label_manual_parameters
    )
    def get(self, request):
        labels = self._get_lables(request)
        return Response({"error": "not", "data": labels})
