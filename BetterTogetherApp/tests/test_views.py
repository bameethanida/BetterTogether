from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from BetterTogetherApp.views import *

class LoginTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('user', 'temp@gmail.com', 'hello12345')

    def test_login_page(self):
        User = get_user_model()
        self.client.login(username='user', password='hello12345')
        response = self.client.get('/profile/', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:index'))
        user = User.objects.get(username='user')
        self.assertEqual(response.context['user'].email, 'temp@gmail.com')
    
    def test_signup_page(self):
        """ Test Signup """
        response = self.client.get('/signup/', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:signup'))

    def test_signout_page(self):
        """ Test Sign Out """
        User = get_user_model()
        self.client.login(username='user', password='hello12345')
        response = self.client.get('/profile/', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:index'))
        user = User.objects.get(username='user')
        self.assertEqual(response.context['user'].email, 'temp@gmail.com')
    
        response = self.client.get('/logout/', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:logout'))

    def test_all_share(self):
        """ Test All Share Page"""
        response = self.client.get('/profile/all_share')
        self.assertEqual(response.status_code, 301)
        self.assertTemplateUsed(redirect('BetterTogetherApp:all_share'))

    def test_profile(self):
        """ Test Profile"""
        User = get_user_model()
        self.client.login(username='user', password='hello12345')
        response = self.client.get('/profile/', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:profile'))

    def test_edit_profile(self):
        """ Test Edit Profile"""
        User = get_user_model()
        self.client.login(username='user', password='hello12345')
        response = self.client.get('/edit_profile/', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:edit_profile'))
        self.assertEqual(response.status_code, 200)

    def test_create_share_ride(self):
        """ Test create share ride event"""
        User = get_user_model()
        self.client.login(username='user', password='hello12345')
        response = self.client.get('/shareride/create', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:create_share_ride'))
        self.assertEqual(response.status_code, 200)

    def test_create_share_promo(self):
        """ Test create share promotion event"""
        User = get_user_model()
        self.client.login(username='user', password='hello12345')
        response = self.client.get('/sharepromo/create', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:create_share_promotion'))
        self.assertEqual(response.status_code, 200)

    def test_create_share_food(self):
        """ Test create share food event"""
        User = get_user_model()
        self.client.login(username='user', password='hello12345')
        response = self.client.get('/sharefood/create', follow=True)
        self.assertTemplateUsed(redirect('BetterTogetherApp:create_share_food'))
        self.assertEqual(response.status_code, 200)

    def test_join_share_food(self):
        """ Test join share promotion event"""
        User = get_user_model()
        sf = ShareFood.objects.create(location_name="BBQ Plaza Major Ratchayothin",location="1839 Phahonyothin Rd, Lat Yao, Chatuchak, Bangkok 10900",
        description="Null", date_time="2019-11-20 08:51:52", num_people=2)
        sf.save()
        self.client.login(username='user', password='hello12345')
        response = self.client.post('sharefood/join/', {'sharefood_id': 1})
        self.assertEqual(response.status_code, 200)

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
        
        