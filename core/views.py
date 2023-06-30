from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from core import forms, models

category = [
    {
        "name": "Marketing",
        "no of vacancy": "20",
        "image": "/media/default/logo.png",
    },
    {
        "name": "Customer Service",
        "no_of_vacancy": "20",
        "image": "/media/default/logo.png",
    },
    {
        "name": "HR",
        "no_of_vacancy": "20",
        "image": "/media/default/logo.png",
    },
    {
        "name": "Project Management",
        "no_of_vacancy": "20",
        "image": "/media/default/logo.png",
    },
]

common_data = {
    "project_name": "Dream_Catcher",
    "page_name": "Home",
}


class HomeView(views.TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        catergories = models.Category.objects.all()
        context["categories"] = catergories
        context.update(common_data)
        return context


class SearchView(views.TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET["keyword"]
        result = models.JobPostModel.objects.filter(post_name__icontains=kw)
        print(result)
        context["results"] = result

        return context


class AdminHomeView(views.TemplateView):
    template_name = "core/admin_home.html"
    extra_context = {
        "project_name": "Dream_Catcher",
        "page_name": "Admin Home",
    }


class EmployerHomeView(views.TemplateView):
    template_name = "core/empr_home.html"
    extra_context = {
        "project_name": "Dream_Catcher",
        "page_name": "employer Home",
    }


class UserHomeView(views.TemplateView):
    template_name = "core/user_home.html"
    extra_context = {
        "project_name": "Dream_Catcher",
        "page_name": "User Home",
    }


class JobPostView(views.CreateView):
    template_name = "core/jobpost/jobpost.html"
    model = models.JobPostModel
    form_class = forms.JobPostForm
    success_url = reverse_lazy("core:jobpost_list")
    context_object_name = "jobpost"


class JobpostListView(views.ListView):
    template_name = "core/jobpost/jobpost_list.html"
    model = models.JobPostModel
    context_object_name = "jobposts"


class JobpostDetailView(views.DetailView):
    template_name = "core/jobpost/jobpost_detail.html"
    model = models.JobPostModel
    context_object_name = "jobpost"


class JobpostUpdateView(views.UpdateView):
    template_name = "core/jobpost/jobpost_update.html"
    model = models.JobPostModel
    form_class = forms.JobPostForm
    success_url = reverse_lazy("core:jobpost_list")


class JobpostDeleteView(views.DeleteView):
    template_name = "core/jobpost/jobpost_delete.html"
    model = models.JobPostModel
    success_url = reverse_lazy("core:jobpost_list")
    context_object_name = "jobpost"


class JobpostListByCategoryView(views.ListView):
    template_name = "core/jobpost/jobpost_list.html"
    model = models.JobPostModel
    context_object_name = "jobposts"

    def get_queryset(self) -> QuerySet[Any]:
        q = super().get_queryset()
        q.filter(id=self.kwargs.get("pk"))
        return q


class DetailView(views.DetailView):
    template_name = "details.html"
    model = models.JobPostModel
    context_object_name = "jobpost"





   

# class Register(views.CreateView):
#       template_name = "core/register.html"
# model = models.JobseekerModel
# form_class = forms.JobseekerForm
#       success_url = reverse_lazy("core:home")


# class LoginView(auth_views.LoginView):
#  template_name = "registration/login.html"
# redirect_authenticated_user = True
