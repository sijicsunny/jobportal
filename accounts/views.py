from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from accounts import forms, models


class ProfileCreateView(LoginRequiredMixin,views.CreateView):
    template_name = "accounts/profile/profile_create.html"
    model = models.ProfileModel
    form_class = forms.ProfileForm
    login_url = reverse_lazy("accounts:login")
    extra_context = {
        "project_name":"Dream_Catcher",
        "page_name":"user profile create",
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EmpprofileCreateView(LoginRequiredMixin,views.CreateView):
    template_name = "accounts/profile/empr_profile.html"
    model = models.EmployerModel
    form_class = forms.EmprProfileForm
    login_url = reverse_lazy("accounts:login")
    extra_context = {
        "project_name":"Dream_Catcher",
        "page_name":"Employer profile create",
       
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    extra_context = {
        "project_name":"Dream_Catcher",
        "page_name":"Login",
       
    }

class LogoutView(auth_views.LogoutView):
        pass
        template_name = "registration/logout.html"
        #success_url = reverse_lazy("core:home")

class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("accounts:password_change_done")

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("accounts:password_change_done")

class PasswordResetView(auth_views.PasswordResetView):
     template_name = "registration/password_reset_form.html"
     success_url = reverse_lazy("accounts:password_reset_done")

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")

class PasswordResetComleteView(auth_views.PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"
      


class SignupView(views.CreateView):
    template_name = "registration/signup.html"
    form_class = forms.UserForm
    success_url = reverse_lazy("accounts:login")

class AddEmployerView(views.CreateView):
    template_name = "registration/add_employer.html"
    model = models.EmployerModel
    form_class = forms.UserForm
    success_url = reverse_lazy("accounts:login")


class EmployerListView(views.ListView):
        template_name = "accounts/employer/employer_list.html"
        model = models.EmployerModel
        context_object_name = "employer"
    
class EmployerDetailView(views.DetailView):
        template_name = "accounts/employer/employer_detail.html"
        model = models.EmployerModel
        context_object_name = "employer"

#class EmployerUpdateView(views.UpdateView):
#        template_name = "accounts/employer/employer_update.html"
#        model = models.EmployerModel
#        form_class = forms.UserForm
#        success_url = reverse_lazy("accounts:employer_list")
    
class EmployerDeleteView(views.DeleteView):
        template_name = "accounts/employer/employer_delete.html"
        model = models.EmployerModel
        success_url = reverse_lazy("accounts:employer_list")
        context_object_name = "employer"   

