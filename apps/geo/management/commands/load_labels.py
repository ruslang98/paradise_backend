import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from apps.geo.models import Category, Label

FIXTURES_PATH = os.path.join(settings.BASE_DIR, "fixtures.csv")


class Command(BaseCommand):
    help = "Заполняем label в базе данных"

    def handle(self, *args, **options):
        LABELS_PATH = os.path.join(settings.BASE_DIR, "markirovka.json")

        with open(LABELS_PATH) as json_file:
            data = json.load(json_file)

            for key, values in data.items():
                print(key)
                print(values)
                category = Category.objects.filter(transliteration=key).last()
                if category:
                    for value in values:
                        Label.objects.create(category=category, title=value)
