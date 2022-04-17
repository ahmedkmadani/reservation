from datetime import date
from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from app.serializers.tables import TableSerializer
from app.serializers.reservation import ReservationsSerializer
from app.models.tables import Tables
from app.models.reservations import Reservations
from app.manager.reservation import IsOpenManager
from app.constants.response import ResposneMsg


class AvailableSlotView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & AllowAny]
    serializer_class = TableSerializer
    queryset = Tables.objects.all()

    def list(self, serializer, *args, **kwargs):

        if not IsOpenManager(
            start_time=self.request.data["start_time"],
            end_time=self.request.data["end_time"],
        ).is_open():
            return Response(
                {"msg": ResposneMsg.RESTURANT_IS_CLOSED}, status=HTTPStatus.OK
            )
        table = self.queryset.filter(seats_number=self.request.data["seats_number"] + 1)
        if not table:
            return Response(
                {"msg": ResposneMsg.NO_AVILABLE_TABLE}, status=HTTPStatus.OK
            )
        else:
            reserved_tables = Reservations.get_resrved_tables(
                table, self.request.data["start_time"], self.request.data["end_time"]
            )
            free_tables = self.queryset.exclude(table_number__in=reserved_tables).all()
            serializer = self.serializer_class(data=free_tables, many=True)
            serializer.is_valid()
            return Response(serializer.data, status=HTTPStatus.OK)


class ReservationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & AllowAny]
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    pagination_class = LimitOffsetPagination
    filterset_fields = ["table_number", "uuid", "customer_phone_number"]

    def create(self, serializer, *args, **kwargs):
        if not IsOpenManager(
            start_time=self.request.data["start_time"],
            end_time=self.request.data["end_time"],
        ).is_open():
            return Response(
                {"msg": ResposneMsg.RESTURANT_IS_CLOSED}, status=HTTPStatus.OK
            )
        elif Reservations.check_duplicate_reservations(
            start_time=self.request.data["start_time"],
            end_time=self.request.data["end_time"],
            table_number=self.request.data["table_number"],
        ):
            return Response(
                {"msg": ResposneMsg.DUPLICATED_RESERVATION}, status=HTTPStatus.OK
            )
        else:
            serializer = self.serializer_class(data=self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def destroy(self, serializer, *args, **kwargs):
        try:
            instance = self.get_object()
            if date.today() == instance.created_at.date():
                self.perform_destroy(instance)
                return Response(
                    {"msg": ResposneMsg.DELETED_SUCCESSFULLY}, status=HTTPStatus.OK
                )
            else:
                return Response(
                    {"msg": ResposneMsg.CANNOT_DELETE_RESERVATION}, status=HTTPStatus.OK
                )
        except Exception as err:
            return Response(
                {"msg": ResposneMsg.RESERVATION_IS_NOT_EXIST}, status=HTTPStatus.OK
            )


class ReservationTodayView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & AllowAny]
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(
            created_at__year=date.today().year,
            created_at__month=date.today().month,
            created_at__day=date.today().day,
        )
        return query_set
