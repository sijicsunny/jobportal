from django.contrib.auth import views as auth_views
from django.urls import path,include
from accounts import views

app_name = "accounts"

urlpatterns = [
    
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    
    path("password_change/",views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/",views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/",views.PasswordResetComleteView.as_view(), name="password_reset_complete"),

    path("profile/create/", views.ProfileCreateView.as_view(), name="profile_create"),
    path("profile/<int:pk>/detail/", views.ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/update/", views.ProfileUpdateView.as_view(), name="profile_update"),
    path("eprofile/", views.EmpprofileCreateView.as_view(), name="profile"),
    path("add/", views.AddEmployerView.as_view(), name="create"),

    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),

    #employers
    path("employers/list/", views.EmployerListView.as_view(), name="employer_list"),
    path("employers/<int:pk>/detail/", views.EmployerDetailView.as_view(), name="employer_detail"),
    path("employers/<int:pk>/update/", views.EmployerUpdateView.as_view(), name="employer_update"),
    path("employers/<int:pk>/delete/", views.EmployerDeleteView.as_view(), name="employer_delete"),

    ]
