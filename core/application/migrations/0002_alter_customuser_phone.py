# Generated by Django 4.2.2 on 2023-06-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="phone",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
