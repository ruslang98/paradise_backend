from django.db import models


class Point(models.Model):
    """Точка переработки """
    address = models.CharField(max_length=128, verbose_name="Адрес")
    longitude = models.CharField(max_length=128, verbose_name="Долгота")
    latitude = models.CharField(max_length=128, verbose_name="Широта")
    description = models.CharField(max_length=255, verbose_name="Описание")
