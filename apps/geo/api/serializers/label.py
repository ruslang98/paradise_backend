from rest_framework import serializers

from apps.geo.models import Label


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["id", "title", "category_id"]
