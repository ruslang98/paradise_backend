# Generated by Django 4.0.3 on 2022-03-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_point_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
