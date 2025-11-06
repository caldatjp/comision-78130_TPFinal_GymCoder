from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import *
from accounts import views


urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_detail, name="profile_detail"),
    path("profile/edit/", profile_edit, name="profile_edit"),
    path("profile/password/", views.cambiar_password, name="password_change"),    
]