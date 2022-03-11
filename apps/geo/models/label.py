from django.db import models

from apps.geo.models import Category


class Label(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
