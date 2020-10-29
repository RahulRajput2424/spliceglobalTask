from django.contrib import admin
from django.urls import path
from spiceApp.views import UserSignupView,UserLoginView

urlpatterns = [
    path('user_signup_view/',UserSignupView.as_view()),
    path('user_login_view/', UserLoginView.as_view()),
]
