from datetime import date
from django.conf import settings
from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from app.serializers.tables import TableSerializer
from app.serializers.reservation import ReservationsSerializer
from app.models.tables import Tables
from app.models.reservations import Reservations
from app.manager.reservation import IsOpenManager
from app.constants.response import ResposneMsg


class AvailableSlotView(APIView):
    permission_classes = [IsAuthenticated & AllowAny]

    def get(self, request):
        seats_number = request.data["seats_number"]
        start_time = request.data["start_time"]
        end_time = request.data["end_time"]

        if not IsOpenManager(start_time=start_time, end_time=end_time).is_open():
            return Response(
                {"msg": ResposneMsg.RESTURANT_IS_CLOSED}, status=HTTPStatus.OK
            )

        table = Tables.objects.filter(seats_number=seats_number + 1).all()
        if not table:
            return Response(
                {"msg": ResposneMsg.NO_AVILABLE_TABLE}, status=HTTPStatus.OK
            )
        else:
            serializer = TableSerializer(data=table, many=True)
            serializer.is_valid()
            return Response(serializer.data, status=HTTPStatus.OK)


class ReservationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & AllowAny]
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    pagination_class = LimitOffsetPagination
    filterset_fields = ["table_number", "uuid", "customer_phone_number"]

    def perform_create(self, serializer):
        if not IsOpenManager(
            start_time=self.request.data["start_time"],
            end_time=self.request.data["end_time"],
        ).is_open():
            return Response(
                {"msg": ResposneMsg.RESERVATION_IS_NOT_EXIST}, status=HTTPStatus.OK
            )
        else:
            serializer = ReservationsSerializer(data=self.request.data)
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
