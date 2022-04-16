from rest_framework import serializers
from app.models.reservations import Reservations


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = "__all__"
