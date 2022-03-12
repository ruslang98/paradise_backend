# django
from django.db import models


class PointCategory(models.Model):
    """Модель для связи многие ко многим для Point и Category"""

    point = models.ForeignKey("geo.Point", on_delete=models.CASCADE)
    category = models.ForeignKey("geo.Category", on_delete=models.CASCADE)
