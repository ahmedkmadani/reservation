from rest_framework import serializers
from app.models.tables import Tables
from app.constants.working_hours import WorkingHours, TimeFormat
from datetime import datetime

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ("pk", "table_number", "seats_number")
        extra_kwargs = {"pk": {"read_only": True}}



class FreeTableSerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    class Meta:
        model = Tables
        fields = ("pk", "table_number", "seats_number", "start_time", "end_time")
        extra_kwargs = {"pk": {"read_only": True}}


    def get_start_time(self, obj):
        return WorkingHours.start_time.time()

    def get_end_time(self, obj):
        return WorkingHours.end_time.time()
