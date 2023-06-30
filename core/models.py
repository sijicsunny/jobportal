from django.db import models

# Create your models here.
# class login(models.Model):
#  Email = models.EmailField(max_length=64)


# class Register(models.Model):
#   Name = models.CharField(max_length=64)
#   Email = models.CharField(max_length=64)
#   Password = models.TextField(max_length=500)
# contact_no = models.(max_length=500)


# category model


class Category(models.Model):
    name = models.CharField(max_length=64)
    no_of_vacancy = models.IntegerField()
    image = models.ImageField(
        upload_to="core/category/image/", default="default/logo.png"
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class JobPostModel(models.Model):
    class CatChoices(models.TextChoices):
        Accounting = "Accounting", "Accounting"
        administrative_assistant = "admini", "Administrative Assistant"
        architect = "architect", "Architect"
        computer_programmer = "cp", "Computer Programmer"
        Construction = "con", "Construction"
        Customer_service = "cs", "Ustomer Service"
        dbadministrator = "dbadmini", "Database Administrator"
        HR = "hr", "Human Resources"
        marketing = "marketing", "Marketing"
        retail = "retail", "Retail"
        sales = "sales", "Sales"

    class QualificationChoices(models.TextChoices):
        Phd = "phd", "PhD"
        PG = "PG", "Post Graduate"
        UG = "UG", "Under Graduate"
        Diploma = "Dip", "Diploma"
        X = "X", "SSLC"

    class EmploymentTypeChoices(models.TextChoices):
        Full_time = "full", "Full Time"
        Part_time = "part", "Part Time"

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    post_name = models.CharField(max_length=64)
    #company_name = models.TextField(max_length=64)
    qualification = models.CharField(
        max_length=64, choices=QualificationChoices.choices
    )
    skills = models.TextField(max_length=60)
    experience = models.IntegerField()
    no_of_vacancy = models.IntegerField()
    location = models.CharField(max_length=255)
    salary = models.IntegerField()
    employment_type = models.CharField(
        max_length=64, choices=EmploymentTypeChoices.choices
    )
    last_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.post_name



