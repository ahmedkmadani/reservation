from django.db import models
from django.conf import settings
from app.models.tables import Tables

import uuid

class Reservations(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    table_number = models.ForeignKey(
        Tables
    )
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=False)
    customer_email = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
