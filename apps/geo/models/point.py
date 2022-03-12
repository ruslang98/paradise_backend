from django.db import models


class Point(models.Model):
    """Точка переработки"""

    address = models.CharField(max_length=128, verbose_name="Адрес")
    lng = models.CharField(max_length=128, verbose_name="Долгота")
    lat = models.CharField(max_length=128, verbose_name="Широта")
    description = models.CharField(max_length=255, verbose_name="Описание")

    @property
    def categories(self):
        return [
            item.category for item in self.pointcategory_set.select_related("category")
        ]
