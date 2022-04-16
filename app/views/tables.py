from rest_framework import viewsets, permissions
from app.models.tables import Tables
from app.serializers.tables import TableSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        return False


class TableViewSet(viewsets.ModelViewSet, IsAdminPermission):
    permission_classes = [IsAuthenticated & IsAdminPermission]
    queryset = Tables.objects.all()
    serializer_class = TableSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
