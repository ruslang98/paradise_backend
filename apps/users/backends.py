# django
from django.contrib.auth.backends import ModelBackend

# project
from apps.users.models import User


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwagrs):
        if username is None:
            username = kwagrs.get(User.USERNAME_FIELD)
        try:
            user = User.objects.get(phone_number=username)
        except User.DoesNotExist:
            return None

        return (
            user
            if user.check_password(password)
            else None
        )