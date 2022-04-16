from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def validate_length(value):
    an_integer = value
    a_string = str(an_integer)
    length = len(a_string)
    if length != 4:
        raise ValidationError("Employee number should be 4 digits")


class User(AbstractUser):
    name = models.CharField(max_length=255)
    employee_number = models.IntegerField(
        unique=True,
        validators=[validate_length],
        error_messages={"required": "Please enter employee number"},
        null=False,
    )
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    username = None
    first_name = None
    last_name = None
    is_staff = None

    USERNAME_FIELD = "employee_number"
    REQUIRED_FIELDS = ["name", "is_admin", "password"]

    def __str__(self) -> str:
        return self.name
