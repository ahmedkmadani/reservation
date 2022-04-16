from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Tables(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table_number = models.IntegerField(
        primary_key=True,
        error_messages={"blank": "Please enter table number"},
        blank=False,
        validators=[MinValueValidator(1)],
    )
    seats_number = models.IntegerField(
        blank=False, validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["table_number"]
