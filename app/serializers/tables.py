from rest_framework import serializers
from app.models.tables import Tables


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ("table_number", "seats_number")
