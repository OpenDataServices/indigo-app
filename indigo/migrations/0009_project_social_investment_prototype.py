# Generated by Django 3.1 on 2020-08-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("indigo", "0008_auto_20200820_1018"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="social_investment_prototype",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
