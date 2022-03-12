from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""

    first_name = models.CharField(max_length=32, null=True, verbose_name="Имя")
    phone_number = models.CharField(
        max_length=32, unique=True, verbose_name="Номер телефона"
    )
    city = models.CharField(max_length=32, null=True, verbose_name="Город")
    is_staff = models.BooleanField(default=False, verbose_name="Сотрудник")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField()

    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.phone_number

    def get_name(self):
        return f"{self.first_name}"