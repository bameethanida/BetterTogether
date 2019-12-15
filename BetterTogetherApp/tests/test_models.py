from django.test import TestCase
from BetterTogetherApp.models import Info, ShareFood, ShareRide, SharePromotion
from django.contrib.auth.models import User
import datetime

class InfoTest(TestCase):
    """Test the Info django models and its get functions"""
    def test_user_info(self):
        """Test user information attributes"""
        user1 = User(first_name="Pawaris", last_name="Wongsalung")
        info1 = Info(user=user1, gender="M", birthday=datetime.date(1998, 8, 12), brief_info="Null")
        self.assertEqual(info1.get_age(), 21)
        self.assertEqual(info1.get_gender(), "M")
        self.assertEqual(info1.get_name(), "Pawaris Wongsalung")
        self.assertEqual(info1.get_brief_info(), "Null")
        self.assertEqual(info1.get_number(), "NOT SET")
        self.assertTrue(isinstance(info1, Info))

        user1 = User(first_name="John", last_name="Newman")
        info1 = Info(user=user1, gender="M", birthday=datetime.date(1996, 8, 12), brief_info="Null")
        self.assertEqual(info1.get_age(), 23)
        self.assertEqual(info1.get_gender(), "M")
        self.assertEqual(info1.get_name(), "John Newman")
        self.assertEqual(info1.get_brief_info(), "Null")
        self.assertEqual(info1.get_number(), "NOT SET")
        self.assertTrue(isinstance(user1, User))

class ShareFoodTest(TestCase):

    def test_sharefood_attributes(self):
        """Test share food attributes"""
        user1 = User(first_name="John", last_name="Newman")
        user1.save()
        info2 = user1.info
        sf = ShareFood(location_name="BBQ Plaza Major Ratchayothin",location="1839 Phahonyothin Rd, Lat Yao, Chatuchak, Bangkok 10900",
        description="Null", date_time="2019-11-20 08:51:52", num_people=2)
        sf.save()
        sf.participants.add(info2)
        self.assertEqual(sf.participants.get(pk=1).get_name(), "John Newman")
        self.assertEqual(sf.get_location_name(), "BBQ Plaza Major Ratchayothin")
        self.assertEqual(sf.get_location(), "Address: 1839 Phahonyothin Rd, Lat Yao, Chatuchak, Bangkok 10900")
        self.assertEqual(sf.get_description(), "Description: Null")
        self.assertEqual(sf.get_time(), "Time to meet up: 2019-11-20 08:51:52")
        self.assertTrue(sf.vacant())
        self.assertEqual(sf.get_hostnum(), "Host Contact (LINE ID or Phone Number) : ")

class ShareRideTest(TestCase):

    def test_shareride_attributes(self):
        """Test share ride attributes"""
        user1 = User(first_name="Mary", last_name="Newman")
        user1.save()
        info1 = user1.info
        sr = ShareRide(location_name="Kasetsart University",location="50 Ngam Wong Wan Road, Ladyaow, Chatuchak Bangkok 10900 Thailand",
        destination_name="Siam Paragon", destination="991 Rama I Rd, Pathum Wan, Pathum Wan District, Bangkok 10330",
        description="Null", date_time="2019-11-20 08:51:52", num_people=2)
        sr.save()
        sr.participants.add(info1)
        self.assertEqual(sr.participants.get(pk=1).get_name(), "Mary Newman")
        self.assertEqual(sr.get_destination_name(), "Siam Paragon")
        self.assertEqual(sr.get_destination(), "Siam Paragon Address: 991 Rama I Rd, Pathum Wan, Pathum Wan District, Bangkok 10330")
        self.assertEqual(sr.get_location_name(), "Kasetsart University")
        self.assertEqual(sr.get_location(), "Kasetsart University Address: 50 Ngam Wong Wan Road, Ladyaow, Chatuchak Bangkok 10900 Thailand")
        self.assertEqual(sr.get_description(), "Description: Null")
        self.assertEqual(sr.get_time(), "Time to meet up: 2019-11-20 08:51:52")
        self.assertTrue(sr.vacant())
        self.assertEqual(sr.get_hostnum(), "Host Contact (LINE ID or Phone Number) : ")

class SharePromotionTest(TestCase):

    def test_sharepromo_attributes(self):
        """Test share promotion attributes"""
        user1 = User(first_name="John", last_name="Newman")
        user1.save()
        info1 = user1.info
        sp = SharePromotion(location_name="Home Pro: Fashion Island",location="589, 10 Thanon Ram Intra, Khan Na Yao, Bangkok 10230", brand="Home Pro",
        description="Buy 3 free 2", date_time="2019-11-20 08:51:52", num_people=2)
        sp.save()
        sp.participants.add(info1)
        self.assertEqual(sp.participants.get(pk=1).get_name(), "John Newman")
        self.assertEqual(sp.get_location_name(), "Meeting Location: Home Pro: Fashion Island")
        self.assertEqual(sp.get_description(), "Description: Buy 3 free 2")
        self.assertEqual(sp.get_brand(), "Name of Store: Home Pro")
        self.assertEqual(sp.get_time(), "Time to meet up: 2019-11-20 08:51:52")
        self.assertTrue(sp.vacant())
        self.assertEqual(sp.get_hostnum(), "Host Contact (LINE ID or Phone Number) : ")