# Generated by Django 4.2.13 on 2024-11-17 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("expiry", models.IntegerField(default=3)),
                (
                    "discount_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "image",
                    models.ImageField(default="default.png", upload_to="products/"),
                ),
                ("in_stock", models.BooleanField(default=True)),
                ("rating", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user_id", models.CharField(default="1", max_length=10)),
                ("expiry_date", models.DateTimeField(blank=True, null=True)),
                (
                    "verified",
                    models.BooleanField(
                        default=False,
                        help_text="Mark this product as verified to display on homepage",
                    ),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("like_new", "Like New"),
                            ("good", "Good"),
                            ("fair", "Fair"),
                            ("needs_repair", "Needs Repair"),
                        ],
                        default="good",
                        help_text="Condition of the product being traded in",
                        max_length=20,
                    ),
                ),
                (
                    "reason_for_trade_in",
                    models.TextField(
                        blank=True,
                        help_text="Reason for trading in the product",
                        null=True,
                    ),
                ),
                (
                    "eco_friendly_certification",
                    models.FileField(
                        blank=True,
                        help_text="Upload eco-friendly certification if applicable",
                        null=True,
                        upload_to="certifications/",
                    ),
                ),
                (
                    "trade_in_preference",
                    models.CharField(
                        choices=[
                            ("recycle", "Recycle"),
                            ("resell", "Resell"),
                            ("donate", "Donate"),
                        ],
                        default="recycle",
                        help_text="User preference for trade-in (recycle, resell, or donate)",
                        max_length=20,
                    ),
                ),
                (
                    "estimated_value",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Estimated trade-in value",
                        max_digits=10,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sale",
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
                ("quantity", models.IntegerField()),
                ("date_sold", models.DateTimeField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sales",
                        to="Shop.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reviews",
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
                ("review", models.TextField()),
                (
                    "rating",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Shop.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InsightProduct",
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
                ("carbon_footprint", models.FloatField()),
                ("water_footprint", models.FloatField()),
                ("energy_consumption", models.FloatField()),
                ("chemical_emissions", models.FloatField()),
                ("waste_recycling_rate", models.FloatField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Shop.product"
                    ),
                ),
            ],
        ),
    ]