from rest_framework.views import APIView
from rest_framework import permissions


class BaseView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]