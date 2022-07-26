from django.contrib import admin
from django.urls import path
from firebase_auth.views import RegisterUser, UserInfo

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('user', UserInfo.as_view()),
]
