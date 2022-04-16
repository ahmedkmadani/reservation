from argparse import Namespace
from unicodedata import name
from django.urls import path, include
from app.views.user import RegisterView
from app.views.tables import TableViewSet
from app.views.reservation import AvailableSlotView, ReservationView
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r"register", RegisterView, basename='register')
router.register(r"table", TableViewSet, basename='table')
router.register(r"reservation", ReservationView)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("available-slots/", AvailableSlotView.as_view()),
    path("", include(router.urls)),
]
