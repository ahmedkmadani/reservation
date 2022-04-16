from datetime import datetime
from django.db import models
from django.conf import settings
from app.models.tables import Tables

import uuid


class Reservations(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    table_number = models.ForeignKey(Tables, on_delete=models.CASCADE)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    customer_phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
