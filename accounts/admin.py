from django.contrib import admin

# Register your models here.

from accounts import models

admin.site.register(models.ProfileModel)
admin.site.register(models.EmployerModel)
admin.site.register(models.JobSeekerModel)