from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("", views.HomeView.as_view(),name="home"),
    path("adminhome/", views.AdminHomeView.as_view(),name="ahome"),
    path("emprhome/", views.EmployerHomeView.as_view(),name="ehome"),
    path("userhome/", views.UserHomeView.as_view(),name="uhome"),
    path("search/", views.SearchView.as_view(),name="search"),
    #jobpost

    path("jobpost/create/", views.JobPostCreateView.as_view(), name="jobpost_create"),
    path("jobposts/list/", views.JobpostListView.as_view(), name="jobpost_list"),
    path("jobposts/list/?category=<int:pk>", views.JobpostListByCategoryView.as_view(), name="jobpost_list_by_category"),
    path("jobposts/<int:pk>/detail/", views.JobpostDetailView.as_view(), name="jobpost_detail"),
    path("jobposts/<int:pk>/update/", views.JobpostUpdateView.as_view(), name="jobpost_update"),
    path("jobposts/<int:pk>/delete/", views.JobpostDeleteView.as_view(), name="jobpost_delete"),
    path("jobposts/<int:pk>/detail/", views.DetailView.as_view(), name="more"),
    path("jobposts/<int:pk>/apply/", views.AppliedJobCreateView.as_view(), name="jobpost_apply"),

    # Applied job
    path("applied-job/<int:pk>/", views.AppliedJobDetailView.as_view(), name="applied_job_detail"),
    path("applied-job/list/", views.AppliedListView.as_view(), name="applied_job_list"),
    path("myapplied/list/", views.MyAppliedListView.as_view(), name="myapplied_list"),

   
   # path("login/", views.LoginView.as_view(), name="login"),
   # path("register/", views.LoginView.as_view(), name="register"),
]

