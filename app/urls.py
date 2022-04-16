from django.contrib import admin
from django.urls import path, include
from app.views.user import RegisterView, LoginView, UserLogoutView
from app.views.tables import TableViewSet
from app.views.reservation import AvailableSlotView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"table", TableViewSet)

urlpatterns = [
    path("login", LoginView.as_view()),
    path("logout", UserLogoutView.as_view()),
    path("register", RegisterView.as_view()),

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),

    path("available-slots/", AvailableSlotView.as_view()),
    path("", include(router.urls)),
]
