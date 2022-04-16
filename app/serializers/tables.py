from rest_framework import serializers
from app.models.tables import Tables


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ("pk","table_number", "seats_number")
        extra_kwargs = {"pk": {"read_only": True}}

