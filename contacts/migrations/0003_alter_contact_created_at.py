# Generated by Django 5.1.3 on 2025-05-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
