from django.test import TestCase
from .models import Info, User, ShareFood, ShareRide, SharePromotion
import datetime

class InfoTest(TestCase):
    """Test the Info django models and its get functions"""

    def test_user_info(self):
        user1 = User(first_name="Pawaris", last_name="Wongsalung")
        info1 = Info(user=user1, gender="M", birthday=datetime.date(1998, 8, 12), brief_info="Null")
        self.assertEqual(info1.get_age(), 21)
        self.assertEqual(info1.get_gender(), "M")
        self.assertEqual(info1.get_name(), "Pawaris Wongsalung")
        self.assertEqual(info1.get_brief_info(), "Null")
        self.assertTrue(isinstance(info1, Info))

        user1 = User(first_name="John", last_name="Newman")
        info1 = Info(user=user1, gender="M", birthday=datetime.date(1996, 8, 12), brief_info="Null")
        self.assertEqual(info1.get_age(), 23)
        self.assertEqual(info1.get_gender(), "M")
        self.assertEqual(info1.get_name(), "John Newman")
        self.assertEqual(info1.get_brief_info(), "Null")
        self.assertTrue(isinstance(user1, User))

class ShareFoodTest(TestCase):

    def test_sharefood_attributes(self):
        user1 = User(first_name="John", last_name="Newman")
        user1.save()
        info1 = Info(user=user1, gender="M", birthday=datetime.date(1996, 8, 12), brief_info="Null")
        info1.save()
        sf = ShareFood(location_name="BBQ Plaza Major Ratchayothin",location="1839 Phahonyothin Rd, Lat Yao, Chatuchak, Bangkok 10900",
        description="Null", date_time="2019-11-20 08:51:52", num_people=2)
        sf.save()
        sf.participants.add(info1)
        self.assertEqual(sf.participants.get(pk=1).get_name(), "John Newman")
        self.assertEqual(sf.get_location_name(), "Meeting Location : BBQ Plaza Major Ratchayothin")

class ShareRideTest(TestCase):

    def test_shareride_attributes(self):
        user1 = User(first_name="Mary", last_name="Newman")
        user1.save()
        info1 = Info(user=user1, gender="M", birthday=datetime.date(1994, 8, 12), brief_info="Null")
        info1.save()
        sr = ShareRide(location_name="Kasetsart University",location="50 Ngam Wong Wan Road, Ladyaow, Chatuchak Bangkok 10900 Thailand",
        destination_name="Siam Paragon", destination="991 Rama I Rd, Pathum Wan, Pathum Wan District, Bangkok 10330",
        description="Null", date_time="2019-11-20 08:51:52", num_people=2)
        sr.save()
        sr.participants.add(info1)
        self.assertEqual(sr.participants.get(pk=1).get_name(), "Mary Newman")
        self.assertEqual(sr.get_location_name(), "Meeting Location : Kasetsart University")

class SharePromotionTest(TestCase):

    def test_sharepromo_attributes(self):
        user1 = User(first_name="John", last_name="Newman")
        user1.save()
        info1 = Info(user=user1, gender="M", birthday=datetime.date(1996, 8, 12), brief_info="Null")
        info1.save()
        sp = SharePromotion(location_name="Home Pro: Fashion Island",location="589, 10 Thanon Ram Intra, Khan Na Yao, Bangkok 10230",
        description="Buy 3 free 2", date_time="2019-11-20 08:51:52", num_people=2)
        sp.save()
        sp.participants.add(info1)
        self.assertEqual(sp.participants.get(pk=1).get_name(), "John Newman")
        self.assertEqual(sp.get_location_name(), "Meeting Location : Home Pro: Fashion Island")
