# Generated by Django 4.0.3 on 2022-03-11 20:53

# django
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0002_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="PointCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="geo.category"
                    ),
                ),
                (
                    "point",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="geo.point"
                    ),
                ),
            ],
        ),
    ]
