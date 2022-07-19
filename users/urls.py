from django.urls import path
from . import views

urlpatterns = [
    # api/users/
    # path("", views.CreateUserView.as_view()),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("profile/", views.UserProfileView.as_view()),
    path("signup/", views.CreateUserView.as_view()),
]
