# Generated by Django 5.1.3 on 2024-12-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("first_name", models.CharField(blank=True, max_length=150)),
                ("last_name", models.CharField(blank=True, max_length=150)),
                ("email", models.EmailField(blank=True, max_length=150)),
                ("address", models.CharField(blank=True, max_length=150)),
                ("basket_history", models.JSONField(default=dict)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[
                            (0, "CREATED"),
                            (1, "PAID"),
                            (2, "ON_WAY"),
                            (3, "DELIVERED"),
                        ],
                        default=0,
                    ),
                ),
            ],
        ),
    ]
