# Generated by Django 5.0.1 on 2024-01-06 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courier", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("payment_date", models.DateTimeField(auto_now_add=True)),
                (
                    "courier",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courier.courier",
                    ),
                ),
            ],
        ),
    ]
