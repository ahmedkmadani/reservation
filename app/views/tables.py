from http import HTTPStatus

from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from app.models.tables import Tables
from app.models.reservations import Reservations
from app.serializers.tables import TableSerializer
from app.constants.response import ResposneMsg


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
    filterset_fields = ["table_number", "seats_number"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, serializer, *args, **kwargs):
        try:
            instance = self.get_object()
            print(instance.pk)
            if Reservations.table_in_reservations(instance.pk):
                return Response(
                    {"msg": ResposneMsg.CANNOT_DELETE_TABLE}, status=HTTPStatus.OK
                )
            else:
                self.perform_destroy(instance)
                return Response(
                    {"msg": ResposneMsg.DELETED_TABLE_SUCCESSFULLY},
                    status=HTTPStatus.OK,
                )
        except Exception as err:
            return Response(
                {"msg": ResposneMsg.TABLE_IS_NOT_EXIST}, status=HTTPStatus.OK
            )
