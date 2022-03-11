from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32, verbose_name="Фракция")
    transliteration = models.CharField(max_length=32, verbose_name="Транслит")