from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.urls import reverse


class ProfileModel(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        TRANSGENDER = "T", "Transgender"

    class QualificationChoices(models.TextChoices):
        Phd = "phd","PhD"
        PG = "PG","Post Graduate"
        UG = "UG","Under Graduate"
        Diploma ="Dip","Diploma"
        X ="X","SSLCC"


    class CourseChoices(models.TextChoices):
            BBA = "Bba","BBA"
            Bcom = "Bcom","Bcom"
            BCA = "Bca","BCA"
            Mcom = "Mcom","Mcom"
            MBA = "Mba","MBA"
            Mca= "Mca","MCA"
            civil = "civil","Civil Engineering"
            Nursing= "Nurse","Bsc Nursing"


            


    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.TextField(max_length=150)
    contact_no = models.BigIntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GenderChoices.choices)
    qualification = models.CharField(max_length=64,choices=QualificationChoices.choices)
    course = models.CharField(max_length=64,choices=CourseChoices.choices)
    institution = models.CharField(max_length=64)
    year_of_passing = models.ImageField()
    percetage = models.IntegerField()
    experience = models.IntegerField()
    skills = models.CharField(max_length=150)
    resume = models.FileField()
    image = models.ImageField(
        upload_to="accounts/profile/image/", default="default/user.png"
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("accounts:profile_detail", args=self.pk)
    

class EmployerModel(models.Model):

    company_name = models.CharField(max_length=64)
    address =  models.TextField(max_length=150)
    contact_no = models.BigIntegerField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("accounts:profile_detail", args=self.pk)