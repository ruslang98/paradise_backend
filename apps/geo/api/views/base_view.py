from rest_framework import permissions
from rest_framework.views import APIView


class BaseView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
