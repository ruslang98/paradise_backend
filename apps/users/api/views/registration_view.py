from drf_yasg.utils import swagger_auto_schema

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api.serializers import RegistrationSerializer
from apps.users.api.services import create_user
from apps.users.api.swagger import registration_responses


class RegistrationView(APIView):

    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        operation_summary="Registration user",
        responses=registration_responses,
        request_body=RegistrationSerializer,
    )
    def post(self, request):
        phone_number = request.data.get("phone_number")
        first_name = request.data.get("first_name")
        password = request.data.get("password")

        user, error = create_user(first_name=first_name, phone_number=phone_number, password=password)
        if error:
            return Response(
                data={"data": None, "error": error},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        return Response(
            data="Success registration",
            status=status.HTTP_200_OK,
        )
