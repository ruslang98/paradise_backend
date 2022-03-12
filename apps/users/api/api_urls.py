from django.urls import path


from apps.users.api.views import (
    LoginView,
    RegistrationView
)

api_urls = [
    path("login/", LoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration"),
]
