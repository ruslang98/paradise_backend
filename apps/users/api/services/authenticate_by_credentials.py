from typing import Union

from django.contrib.auth import authenticate

from apps.users.models import User


def authenticate_by_credentials(phone_number: str, password: str) -> Union[tuple[None, str], tuple[User, None]]:
    """Аутентификация пользователя по номеру телефона и паролю"""

    user = authenticate(phone_number=phone_number, password=password)
    if not user:
        return None, "Invalid credentials!"

    if not user.is_active:
        return None, "User is not active!"

    return user, None
