from rest_framework.response import Response

from apps.geo.api.views import BaseView
from apps.geo.models import Category


class CategoryList(BaseView):
    def _get_categories(self):
        categories = Category.objects.values("id", "title", "transliteration")
        return categories

    def get(self, request):
        categories = self._get_categories()
        return Response({"error": "not", "data": categories})
