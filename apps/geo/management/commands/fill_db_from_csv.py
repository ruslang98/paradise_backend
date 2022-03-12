# stdlib
import csv
import os

# django
from django.conf import settings
from django.core.management import BaseCommand

# project
from apps.geo.models import Category, Point, PointCategory

FIXTURES_PATH = os.path.join(settings.BASE_DIR, "fixtures.csv")

categories_transliteration = {
    "plastik": "Пластик",
    "metal": "Металл",
    "bymaga": "Бумага",
    "steklo": "Стекло",
    "odegda": "Одежда",
    "batareiki": "Батарейки",
    "lampochki": "Лампочки",
    "technika": "Техника",
    "zubnie_shetki": "Зубные щетки",
    "gradusniki": "Градусники",
    "krishechki": "Крышечки",
    "inoe": "Иное",
    "shini": "Шины",
}


class Command(BaseCommand):
    help = "Заполняем записи точек и категорий в базе данных"

    def handle(self, *args, **options):
        with open(FIXTURES_PATH, newline="") as fixture:
            reader = csv.reader(fixture)
            for row in reader:
                try:
                    latitude_from_csv = row[1].replace(" ", "").split(",")[0]
                    longitude_from_csv = row[1].replace(" ", "").split(",")[1]
                    categories_from_csv = row[18].replace(" ", "").split(",")
                except Exception:
                    continue

                address = row[0].split("\n")[0]

                new_point = Point.objects.create(
                    description=row[0],
                    lat=latitude_from_csv,
                    lng=longitude_from_csv,
                    address=address,
                )

                for category_transliteration in categories_from_csv:
                    new_category, _ = Category.objects.get_or_create(
                        transliteration=category_transliteration,
                        title=categories_transliteration[category_transliteration],
                    )

                    PointCategory.objects.create(
                        point_id=new_point.id, category_id=new_category.id
                    )
