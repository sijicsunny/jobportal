from typing import Any
from django import forms
from accounts import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.ProfileModel
        exclude = ("user", "status")


class EmprProfileForm(forms.ModelForm):
    class Meta:
        model = models.EmployerModel
        exclude = ("user", "status")


class UserForm(UserCreationForm):
    is_employer = forms.BooleanField(label="Are you an Emloyer?", required=False)
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit)
        is_employer = self.cleaned_data["is_employer"]
        if is_employer:
            employer = models.EmployerModel.objects.create(user=user)
        else:
            jobseeker = models.JobSeekerModel.objects.create(user=user)
        return user
