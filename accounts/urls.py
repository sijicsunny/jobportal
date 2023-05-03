from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileCreateView.as_view(), name="uprofile"),
    path("eprofile/", views.EmpprofileCreateView.as_view(), name="profile"),
    path("add/", views.AddEmployerView.as_view(), name="create"),
    ]
