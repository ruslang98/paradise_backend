from rest_framework import serializers

from apps.geo.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id", "title", "transliteration"]
        model = Category
