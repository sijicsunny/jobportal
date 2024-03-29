# Generated by Django 4.2.3 on 2023-08-09 16:56

import accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_employermodel_contact_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilemodel",
            name="experience",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="profilemodel",
            name="percentage",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="profilemodel",
            name="year_of_passing",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(2010),
                    accounts.models.ProfileModel.current_year_validator,
                ]
            ),
        ),
    ]
