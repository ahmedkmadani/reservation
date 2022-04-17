from django.core.management.base import BaseCommand
from app.models.user import User as UserModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    """
    Command to seed db with admin user
    """

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("STARTED"))

        user = UserModel.objects.filter(employee_number=1234).first()
        if user:
            self.stdout.write(self.style.ERROR("USER IS ALREADY IN THE DB"))
        else:
            data = {
                "employee_number": 1234,
                "name": "admin",
                "email": "admin@mail.com",
                "is_admin": True,
                "is_superuser": True,
            }
            instance = User(**data)
            instance.set_password("password")
            instance.save()

        self.stdout.write(self.style.NOTICE("FINISHED"))
