from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from app.models.user import User
from django.urls import reverse

# Create your tests here.


class UserTest(APITestCase):
    def test_create_admin(self):
        self.testuser1 = User.objects.create(password="test", employee_number="1234")

        # url = reverse('blog_api:listcreate')
        response = self.client.login(
            password=self.testuser1.password, employee_number="1234"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
