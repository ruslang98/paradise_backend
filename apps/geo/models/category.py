from django.db import models


class Category(models.Model):
    """Модель категорий"""

    title = models.CharField(max_length=32, verbose_name="Фракция")
    transliteration = models.CharField(max_length=32, verbose_name="Транслит")

    @property
    def points(self):
        return [item.point for item in self.pointcategory_set.select_related("point")]
