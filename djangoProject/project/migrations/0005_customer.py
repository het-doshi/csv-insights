# Generated by Django 4.1.13 on 2024-09-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0004_purchase_delete_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customer_id", models.AutoField(primary_key=True, serialize=False)),
                ("customer_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=15)),
            ],
        ),
    ]
