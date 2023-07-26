# Generated by Django 4.2.3 on 2023-07-26 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=64)),
                ("no_of_vacancy", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        default="default/logo.png", upload_to="core/category/image/"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobPostModel",
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
                ("post_name", models.CharField(max_length=64)),
                ("company_name", models.CharField(max_length=64)),
                (
                    "qualification",
                    models.CharField(
                        choices=[
                            ("phd", "PhD"),
                            ("PG", "Post Graduate"),
                            ("UG", "Under Graduate"),
                            ("Dip", "Diploma"),
                            ("X", "SSLC"),
                        ],
                        max_length=64,
                    ),
                ),
                ("skills", models.TextField(max_length=60)),
                ("experience", models.IntegerField()),
                ("no_of_vacancy", models.IntegerField()),
                ("location", models.CharField(max_length=255)),
                ("salary", models.IntegerField()),
                (
                    "employment_type",
                    models.CharField(
                        choices=[("full", "Full Time"), ("part", "Part Time")],
                        max_length=64,
                    ),
                ),
                ("last_date", models.DateField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AppliedModel",
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
                (
                    "resume",
                    models.FileField(
                        blank=True, null=True, upload_to="core/applied/resumes/"
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "jobpost",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.jobpostmodel",
                    ),
                ),
            ],
        ),
    ]