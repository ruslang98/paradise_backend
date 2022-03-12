from rest_framework import serializers


class RegistrationSerializer(serializers.Serializer):
    """Сериализатор для регистрации пользователя"""

    phone_number = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)