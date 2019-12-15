from django.test import Client, TestCase
from django.urls import reverse
from BetterTogetherApp.forms import *
from BetterTogetherApp.models import *


class BetterTogetherTestsForm(TestCase):
    def test_valid_form(self):
        sf = ShareFood.objects.create(location_name="BBQ Plaza Major Ratchayothin",location="1839 Phahonyothin Rd, Lat Yao, Chatuchak, Bangkok 10900",
        description="Null", date_time="2019-11-20 08:51:52", num_people=2)
        data = {'location_name': sf.location_name, 'location': sf.location,
        'description': sf.description, 'date_time': sf.date_time, 'num_people': sf.num_people}
        form = ShareFoodForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        sf = ShareFood.objects.create(location_name="BBQ Plaza Major Ratchayothin",location="1839 Phahonyothin Rd, Lat Yao, Chatuchak, Bangkok 10900",
         date_time="AAA", num_people=2)
        data = {'location_name': sf.location_name, 'location': sf.location,
        'description': sf.description, 'date_time': sf.date_time, 'num_people': sf.num_people}
        form1 = ShareFoodForm(data=data)
        self.assertFalse(form1.is_valid())