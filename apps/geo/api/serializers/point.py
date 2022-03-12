from rest_framework import serializers

from apps.geo.models import Category, Point


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PointSerializer(serializers.ModelSerializer):

    """Сериализатор для модели Point"""

    categories = CategorySerializer(many=True)

    class Meta:
        model = Point
        fields = ["id", "address", "lng", "lat", "description", "categories"]
