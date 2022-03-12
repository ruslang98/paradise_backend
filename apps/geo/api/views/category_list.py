from rest_framework.response import Response

from apps.geo.api.serializers import CategorySerializer
from apps.geo.api.views import BaseView
from apps.geo.models import Category


class CategoryList(BaseView):
    def _get_categories(self):
        categories = Category.objects.all()
        return categories

    def get(self, request):
        categories = self._get_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response({"error": "not", "data": serializer.data})
