from django.shortcuts import render, redirect
from django.views import generic as views 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from core import forms, models

category = [
    {
        "name":"Marketing",
        "no of vacancy":"20",
        "image":"/media/default/logo.png",
    },
        {
        "name":"Customer Service",
        "no_of_vacancy":"20",
        "image":"/media/default/logo.png",
    },
        {
        "name":"HR",
        "no_of_vacancy":"20",
        "image":"/media/default/logo.png",
    },
        {
        "name":"Project Management",
        "no_of_vacancy":"20",
        "image":"/media/default/logo.png",
    },

]



class HomeView(views.TemplateView):
    template_name = "core/home.html"
    extra_context = {
        "project_name":"Dream_Catcher",
        "page_name":"Home",
         "categories" :"categories",
    }

class AdminHomeView(views.TemplateView):
    template_name = "core/admin_home.html"
    extra_context = {
        "project_name":"Dream_Catcher",
        "page_name":"Admin Home",
        
    }

class EmployerHomeView(views.TemplateView):
    template_name = "core/empr_home.html"
    extra_context = {
        "project_name":"Dream_Catcher",
        "page_name":"employer Home",
        
    }

class UserHomeView(views.TemplateView):
    template_name = "core/user_home.html"
    extra_context = {
        "project_name":"Dream_Catcher",
        "page_name":"User Home",
        
    }

class JobPostView(views.CreateView):
        template_name = "core/jobpost/jobpost.html"
        model = models.JobPostModel
        form_class = forms.JobPostForm
        success_url = reverse_lazy("core:ehome")




#class Register(views.CreateView):
 #       template_name = "core/register.html"
        #model = models.JobseekerModel
        #form_class = forms.JobseekerForm
 #       success_url = reverse_lazy("core:home")


#class LoginView(auth_views.LoginView):
  #  template_name = "registration/login.html"
  # redirect_authenticated_user = True
