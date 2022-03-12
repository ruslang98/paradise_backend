from django.urls import path

# project
from apps.users.api.views import (
    LoginView,
)

api_urls = [
    path("login/", LoginView.as_view(), name="login"),
]
