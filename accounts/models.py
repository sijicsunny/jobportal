import datetime
from typing import Any, Iterable, List

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import QuerySet
from django.db.models.manager import BaseManager
from django.urls import reverse


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserModel(TimestampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class QualificationModel(TimestampedModel):
    name = models.CharField(max_length=64)
    course_name = models.CharField(max_length=64)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}. {self.course_name}"


# user profile
class ProfileModel(models.Model):
    def current_year_validator(value):
        if value > datetime.date.today().year:
            raise ValidationError("Year cannot be in the future.")

    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        TRANSGENDER = "T", "Transgender"

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.TextField(max_length=150)
    contact_no = models.BigIntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GenderChoices.choices)
    qualification = models.ForeignKey(
        QualificationModel, on_delete=models.SET_NULL, blank=True, null=True
    )
    institution = models.CharField(max_length=64)
    year_of_passing = models.IntegerField(
        validators=[
            MinValueValidator(2010),  # Change the minimum value as needed
            current_year_validator,  # Change the maximum value as needed
        ]
    )
    percentage = models.DecimalField(decimal_places=2, max_digits=5)
    experience = models.DecimalField(decimal_places=2, max_digits=5)
    skills = models.TextField(max_length=150, blank=True, null=True)
    resume = models.FileField(
        upload_to="accounts/profile/resumes/", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="accounts/profile/image/",
        default="default/user.png",
    )
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("accounts:profile_detail", args=(self.pk,))


# employer profile
class EmployerModel(models.Model):
    company_name = models.CharField(max_length=64)
    address = models.TextField(max_length=150)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("accounts:profile_detail", args=(self.pk,))

    def __str__(self) -> str:
        return self.company_name or "Not Defined"

    @property
    def jobposts(self) -> BaseManager[Any]:
        posts = getattr(self.user, "jobposts", QuerySet())
        return posts


class JobSeekerModel(BaseUserModel):
    profile = models.OneToOneField(
        ProfileModel, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.user.username}"
