import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from app.models.user import User
from app.serializers.user import UserSerializers
from app.views.tables import IsAdminPermission


class RegisterView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & IsAdminPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = LimitOffsetPagination
    filterset_fields = ["employee_number"]
