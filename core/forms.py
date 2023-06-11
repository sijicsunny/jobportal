from django import forms
from core import models


#class RegisterForm(forms.ModelForm):
 #   class Meta:
 #       model = models.Register
  #      fields = ["Name","Email","Password"]


class JobPostForm(forms.ModelForm):
    class Meta:
        model = models.JobPostModel
        fields =["category","post_name","qualification","skills","experience","no_of_vacancy","location","salary","employment_type","last_date"]
        
