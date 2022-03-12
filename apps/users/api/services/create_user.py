from typing import Union

from apps.users.models import User


def create_user(phone_number: str, first_name: str, password: str) -> Union[tuple[None, str], tuple[User, None]]:
    """Создание пользователя"""

    if User.objects.filter(phone_number=phone_number).exists():
        return None, "User with given phone number already exists"

    user = User.objects.create_user(first_name=first_name, phone_number=phone_number)
    user.set_password(password)
    user.is_active = False
    user.save()