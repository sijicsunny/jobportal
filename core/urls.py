from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("home", views.HomeView.as_view(),name="home"),
    path("adminhome", views.AdminHomeView.as_view(),name="ahome"),
    path("emprhome", views.EmployerHomeView.as_view(),name="ehome"),
    path("userhome", views.UserHomeView.as_view(),name="uhome"),
    path("jobpost/create/", views.JobPostView.as_view(), name="jobpost"),
   


   # path("login/", views.LoginView.as_view(), name="login"),
   # path("register/", views.LoginView.as_view(), name="register"),
]
