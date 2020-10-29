from django.contrib import admin
from django.urls import path
from spiceApp.views import UserSignupView

urlpatterns = [
    path('user_signup_view/',UserSignupView.as_view()),
]
