# Generated by Django 4.0.3 on 2022-03-12 00:13

# django
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0006_rename_latitude_point_lat_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="point",
            old_name="long",
            new_name="lng",
        ),
    ]
