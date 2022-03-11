from django.db import models


class Point(models.Model):
    """Точка переработки"""

    address = models.CharField(max_length=128, verbose_name="Адрес")
    longitude = models.CharField(max_length=128, verbose_name="Долгота")
    latitude = models.CharField(max_length=128, verbose_name="Широта")
    description = models.TextField(verbose_name="Описание")

    @property
    def categories(self):
        return [
            item.category for item in self.pointcategory_set.select_related("category")
        ]
