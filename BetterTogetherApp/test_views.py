from django.test import Client, TestCase
from django.urls import reverse
from .views import *

class BetterTogetherTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)