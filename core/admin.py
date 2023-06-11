from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.JobPostModel)
admin.site.register(models.Category)