from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api.services import authenticate_by_credentials
from apps.users.api.serializers import LoginSerializer
from apps.users.api.swagger import login_responses


class LoginView(APIView):

    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        operation_summary="Login user",
        responses=login_responses,
        request_body=LoginSerializer,
    )
    def post(self, request):

        phone_number = request.data.get("phone_number")
        password = request.data.get("password")

        user, error = authenticate_by_credentials(phone_number, password)

        if error:
            return Response(
                data={"error": error}, status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        if user.is_authenticated:
            logout(request)

        login(request, user)

        return Response(
            {"data": "Success login", "error": None}, status=status.HTTP_200_OK
        )