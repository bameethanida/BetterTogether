from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save


class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    gender = models.CharField('Gender (F or M)', max_length=1)
    birthday = models.DateField(null=True, blank=True)
    brief_info = models.TextField('Background Infomation', default="")
    phone_num = models.CharField('Phone Number', max_length=10, default=0)
    twitter = models.TextField('Twitter', blank=True)

    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_age(self):
        return int((dt.date.today() - self.birthday).days/365.25)

    def get_gender(self):
        return self.gender

    def get_brief_info(self):
        return self.brief_info

    def get_gender(self):
        return self.gender

    def get_number(self):
        return self.phone_num

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Info.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.info.save()


class ShareFood(models.Model):
    location_name = models.TextField('Location Name', default="",max_length=80)
    location = models.TextField('Location', default="",max_length=80)
    description = models.TextField('Description', default="",max_length=100)
    date_time = models.DateTimeField('Date and Time',auto_now=True)
    participants = models.ManyToManyField(Info)
    num_people = models.IntegerField("Number of people", default=2)
    host = models.CharField("Host's Name", default="", max_length=30)
    host_gender = models.CharField('Host Gender (F or M)', max_length=1)
    host_number = models.CharField("Host's Phone Number", max_length=10, default="")
    full = models.BooleanField(default=False)

    def get_location_name(self):
        return f"{self.location_name}"

    def get_location(self):
        return f"Address: {self.location}"

    def get_description(self):
        return f"Description: {self.description}"

    def get_time(self):
        return f"Time to meet up: {str(self.date_time)}"

    def vacant(self):
        return len(self.participants.all()) < self.num_people

    def get_hostnum(self):
        return f"Host Contact (LINE ID or Phone Number) : {self.host_number}"

    def get_hostgen(self):
        return f"Host Gender: {self.host_gender}"

    

class ShareRide(models.Model):
    myDate = datetime.now()
    formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

    location_name = models.TextField('Location Name', default="",max_length=80)
    location = models.TextField('Location', default="", max_length=80)
    destination_name = models.TextField('Destination Name', default="",max_length=80)
    destination = models.TextField('Destination', default="",max_length=80)
    description = models.TextField('Description', default="", max_length=100)
    date_time = models.DateTimeField('Date and Time', default=formatedDate)
    participants = models.ManyToManyField(Info)
    num_people = models.IntegerField("Number of people", default=2)
    host = models.CharField("Host's Name", default="", max_length=30)
    host_gender = models.CharField('Host Gender (F or M)', max_length=1)
    host_number = models.CharField("Host's Phone Number", max_length=10, default="")
    full = models.BooleanField(default=False)

    def get_destination_name(self):
        return f"{self.destination_name}"

    def get_destination(self):
        return f"{self.destination_name} Address: {self.destination}"

    def get_location_name(self):
        return f"{self.location_name}"

    def get_location(self):
        return f"{self.location_name} Address: {self.location}"

    def get_description(self):
        return f"Description: {self.description}"

    def get_time(self):
        return f"Time to meet up: {str(self.date_time)}"

    def vacant(self):
        return len(self.participants.all()) < self.num_people

    def del_self(self):
        share = self
        self.delete()
        self.save()

    def get_hostnum(self):
        return f"Host Contact (LINE ID or Phone Number) : {self.host_number}"

    def get_hostgen(self):
        return f"Host Gender: {self.host_gender}"

class SharePromotion(models.Model):
    location_name = models.TextField('Location Name', default="",max_length=80)
    location = models.TextField('Location', default="",max_length=80)
    brand = models.TextField('Brand', default="",max_length=80)
    description = models.TextField('Description', default="",max_length=100)
    date_time = models.DateTimeField('Date and Time')
    participants = models.ManyToManyField(Info)
    num_people = models.IntegerField("Number of people", default=2)
    host = models.CharField("Host's Name", default="", max_length=30)
    host_gender = models.CharField('Host Gender (F or M)', max_length=1)
    host_number = models.CharField("Host's Phone Number", max_length=10, default="")
    full = models.BooleanField(default=False)

    def get_location_name(self):
        return f"Meeting Location: {self.location_name}"

    def get_brand(self):
        return f"Name of Store: {self.brand}"

    def get_description(self):
        return f"Description: {self.description}"

    def get_time(self):
        return f"Time to meet up: {str(self.date_time)}"

    def vacant(self):
        return len(self.participants.all()) < self.num_people

    def get_hostnum(self):
        return f"Host Contact (LINE ID or Phone Number) : {self.host_number}"

    def get_hostgen(self):
        return f"Host Gender: {self.host_gender}"
