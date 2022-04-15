from django.contrib import admin
from django.urls import path, include
from app.views.user import RegisterView, LoginView, UserLogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', UserLogoutView.as_view())
]
