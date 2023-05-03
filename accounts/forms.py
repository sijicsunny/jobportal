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
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]

class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]