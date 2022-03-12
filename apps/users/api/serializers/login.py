from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Сериализатор для аутентификации пользователя"""

    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True)