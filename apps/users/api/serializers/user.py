from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "phone_number",
            "city",
            "is_staff",
            "qr_code",
            "is_active",
            "date_joined",
            "last_login",
        ]