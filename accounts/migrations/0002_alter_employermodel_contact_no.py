# Generated by Django 4.2.3 on 2023-08-04 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employermodel",
            name="contact_no",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
