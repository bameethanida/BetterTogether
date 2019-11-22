from django.test import Client, TestCase
from django.urls import reverse
from .views import *

class BetterTogetherTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(redirect('BetterTogetherApp:index'))
        response = self.client.get('/homepage/')
        self.assertEqual(response.status_code, 404)

    def test_views(self):
        response = self.client.get('/shareride/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(redirect('BetterTogetherApp:share_ride_index1'))
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 404)
        