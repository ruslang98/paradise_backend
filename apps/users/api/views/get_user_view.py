from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


from apps.users.api.serializers import UserSerializer


class GetUserView(APIView):

    authentication_classes = (SessionAuthentication,)

    def get(self, request: Request):
        user = request.user
        serializer = UserSerializer(user)

        if not request.session or not request.session.session_key:
            request.session.save()

        if not user.is_authenticated:
            return Response(
                data={"error": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.data)
