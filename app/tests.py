from django.test import TestCase
from app.management.commands.create_admin import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from app.models.user import User as UserModel
from django.contrib.auth import get_user_model

User = get_user_model()

#TODDO: REFACTOR USER CREATE TO OVERCOME DRY

class TablesTest(APITestCase):

    def test_admin_create_table(self):

        """
        Test user admin to create table
        """

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

        self.client.force_authenticate(instance)

        table_data = {
            "table_number": 1,
            "seats_number": 2
        }

        url = reverse('table-list')
        response = self.client.post(url, data=table_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_view_tables(self):

        """
        Test user admin to view tables
        """
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

        self.client.force_authenticate(instance)

        url = reverse('table-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_view_tables(self):

        """
        Test user employee to create table
        """

        data = {
            "employee_number": 1111,
            "name": "user",
            "email": "admin@mail.com",
            "is_admin": False,
        }
        instance = User(**data)
        instance.set_password("password")
        instance.save()

        self.client.force_authenticate(instance)

        url = reverse('table-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_create_table(self):

        """
        Test user employee to view tables
        """

        data = {
            "employee_number": 1111,
            "name": "user",
            "email": "admin@mail.com",
            "is_admin": False,
        }
        instance = User(**data)
        instance.set_password("password")
        instance.save()

        self.client.force_authenticate(instance)

        table_data = {
            "table_number": 1,
            "seats_number": 2
        }

        url = reverse('table-list')
        response = self.client.post(url, data=table_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RegisterTest(APITestCase):

    """
    Test user admin to create employee user
    """

    def test_create_user(self):

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

        self.client.force_authenticate(instance)

        user_data = {
                "name": "user",
                "email": "user@mail.com",
                "password": "test",
                "employee_number": 1233
            }

        url = reverse('register-list')
        response = self.client.post(url, data=user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
