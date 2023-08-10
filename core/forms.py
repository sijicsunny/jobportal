import datetime
from django import forms
from core import models


# class RegisterForm(forms.ModelForm):
#   class Meta:
#       model = models.Register
#      fields = ["Name","Email","Password"]


class JobPostForm(forms.ModelForm):
    last_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "min": str(datetime.date.today())}
        )
    )
    company_name = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))

    class Meta:
        model = models.JobPostModel
        fields = [
            "category",
            "post_name",
            "company_name",
            "qualification",
            "skills",
            "experience",
            "no_of_vacancy",
            "location",
            "salary",
            "employment_type",
            "last_date",
        ]


class AppliedForm(forms.ModelForm):
    class Meta:
        model = models.AppliedModel
        fields = ["resume"]
