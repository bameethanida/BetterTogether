from django.test import Client, TestCase
from django.urls import reverse
from BetterTogetherApp.views import *

class BetterTogetherTests(TestCase):
    def test_homepage(self):
        """ Test Homepage """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(redirect('BetterTogetherApp:index'))
        response = self.client.get('/homepage/')
        self.assertEqual(response.status_code, 404)

    def test_sign_in(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(redirect('BetterTogetherApp:login'))

    def test_share_ride_views(self):
        response = self.client.get('/shareride/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(redirect('BetterTogetherApp:share_ride_index1'))
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 404)

    def test_share_ride_create(self):
        response = self.client.get('/shareride/create')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('BetterTogetherApp:share_ride_index1'))
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 404)
        
    def test_share_promo_views(self):
        response = self.client.get('/sharepromo/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(redirect('BetterTogetherApp:share_promotion_index1'))
        response = self.client.get('/sharepromotion/')
        self.assertEqual(response.status_code, 404)

    def test_share_promo_create(self):
        response = self.client.get('/sharepromo/create')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('BetterTogetherApp:share_promotion_index1'))
        response = self.client.get('/sharepromotion/')
        self.assertEqual(response.status_code, 404)
        
    def test_share_food_views(self):
        response = self.client.get('/sharefood/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/sharefood1/')
        self.assertEqual(response.status_code, 404)

    def test_share_food_create(self):
        response = self.client.get('/sharefood/create')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('BetterTogetherApp:login'))
        response = self.client.get('/sharefood1/')
        self.assertEqual(response.status_code, 404)
        
        