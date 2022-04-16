from app.serializers.tables import TableSerializer
from rest_framework import serializers
from app.models.reservations import Reservations
from app.constants.working_hours import TimeFormat


class ReservationsSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(input_formats=([TimeFormat.time_format]))
    end_time = serializers.TimeField(input_formats=([TimeFormat.time_format]))
    table = TableSerializer(read_only=True, many=True)

    class Meta:
        model = Reservations
        fields = "__all__"
        extra_kwargs = {"table": {"read_only": True}}
