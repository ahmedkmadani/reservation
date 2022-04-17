from datetime import datetime
from django.db import models
from app.models.tables import Tables
from app.manager.reservation import ConvertTime
import uuid

from django.db.models import Q


class Reservations(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    table_number = models.ForeignKey(Tables, on_delete=models.CASCADE)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    customer_phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    @classmethod
    def get_resrved_tables(cls, table, start_time, end_time):
        """
        get all reserved tables based on start/end
        time and table free for that customer
        """
        start_time_, end_time_ = ConvertTime(
            start_time=start_time, end_time=end_time
        ).convertTo24()
        filter_params = dict(start_time__lte=start_time_, end_time__gte=end_time_)
        reserved_tables = (
            cls.objects.select_related("table_number")
            .filter(**filter_params, table_number__pk__in=table)
            .all()
        )
        return reserved_tables

    @classmethod
    def check_duplicate_reservations(cls, start_time, end_time, table_number):
        """
        check if table is reserved at same start/end time
        """
        start_time_, end_time_ = ConvertTime(
            start_time=start_time, end_time=end_time
        ).convertTo24()
        is_exists = cls.objects.filter(
            Q(start_time=start_time_)
            & Q(end_time=end_time_)
            & Q(table_number=table_number)
        ).exists()
        return is_exists

    @classmethod
    def table_in_reservations(cls, pk):
        """
        check if table is in Reservations
        """
        is_exists = cls.objects.filter(table_number=pk).exists()
        return is_exists
