from typing import Any, Dict

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from core import forms, models

# from accounts import forms, models
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


class AdminHomeView(LoginRequiredMixin, PermissionRequiredMixin, views.TemplateView):
    template_name = "core/admin_home.html"
    extra_context = {
        "project_name": "Dream_Catcher",
        "page_name": "Admin Home",
    }
    permission_required = []
    permission_denied_message = "You are not allowed to view this page"

    def has_permission(self) -> bool:
        permitted = self.request.user.is_superuser and super().has_permission()
        return permitted


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


class JobPostCreateView(LoginRequiredMixin, views.CreateView):
    template_name = "core/jobpost/jobpost_create.html"
    model = models.JobPostModel
    form_class = forms.JobPostForm
    success_url = reverse_lazy("core:jobpost_list")
    context_object_name = "jobpost"

    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        if hasattr(self.request.user, "employermodel"):
            kwargs.update(
                {
                    "initial": {
                        "company_name": self.request.user.employermodel.company_name,
                    }
                }
            )
        return kwargs

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class JobpostListView(views.ListView):
    template_name = "core/jobpost/jobpost_list.html"
    model = models.JobPostModel
    context_object_name = "jobposts"

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()

        employer = getattr(self.request.user, "employermodel", False)
        if employer:
            qs = qs.filter(posted_by=self.request.user)

        return qs


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


class AppliedJobCreateView(LoginRequiredMixin, views.CreateView):
    template_name = "applied.html"
    model = models.AppliedModel
    form_class = forms.AppliedForm
    context_object_name = "jobpost"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        jobpost_id = self.kwargs.get("pk")
        self.jobpost = models.JobPostModel.objects.get(id=jobpost_id)
        context["jobpost"] = self.jobpost
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        jobpost_id = self.kwargs.get("pk")
        self.jobpost = models.JobPostModel.objects.get(id=jobpost_id)
        appliedjob = models.AppliedModel.objects.filter(jobpost__id=jobpost_id)
        if not appliedjob.exists():
            form.instance.user = self.request.user
            form.instance.jobpost = self.jobpost
            return super().form_valid(form)
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        jobpost_id = self.kwargs.get("pk")
        appliedjob = models.AppliedModel.objects.filter(jobpost__id=jobpost_id).first()
        return reverse_lazy("core:applied_job_detail", kwargs={"pk": appliedjob.id})


class AppliedJobDetailView(LoginRequiredMixin, views.DetailView):
    template_name = "preview.html"
    model = models.AppliedModel
    context_object_name = "appliedjob"


class AppliedListView(LoginRequiredMixin, views.ListView):
    template_name = "applied_list.html"
    model = models.AppliedModel
    context_object_name = "appliedjobs"

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        employer = getattr(self.request.user, "employermodel", False)
        jobseeker = getattr(self.request.user, "jobseekermodel", False)
        if employer:
            jobposts = employer.jobposts.values_list("id", flat=True)
            qs = qs.filter(jobpost__id__in=jobposts)
        elif jobseeker:
            qs = qs.filter(user=self.request.user)

        return qs


class MyAppliedListView(views.ListView):
    template_name = "myapplied_list.html"
    model = models.AppliedModel
    context_object_name = "appliedjobs"


# class Register(views.CreateView):
#       template_name = "core/register.html"
# model = models.JobseekerModel
# form_class = forms.JobseekerForm
#       success_url = reverse_lazy("core:home")


# class LoginView(auth_views.LoginView):
#  template_name = "registration/login.html"
# redirect_authenticated_user = True
