# Generated by Django 4.2 on 2024-11-18 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="Email",
            field=models.EmailField(default="test@ecowave.ca", max_length=254),
        ),
    ]