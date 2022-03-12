from rest_framework import serializers

from apps.geo.models import Point


class PointSerializer(serializers.Serializer):

    """Сериализатор для модели Point"""

    class Meta:
        model = Point
        fields = ["id", "address", "lng", "lat", "description"]
