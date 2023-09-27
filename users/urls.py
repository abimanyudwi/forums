from django.contrib import admin
from django.urls import path
from . import views

# from django.contrib.auth import views as authentication_views

app_name = "users"

urlpatterns = [
    # path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update-profile/", views.update_profile, name="update-profile"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    # path("forum/", views.forum, name="forum"),
]
