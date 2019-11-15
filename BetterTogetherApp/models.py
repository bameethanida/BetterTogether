from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import datetime

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField('Gender (F or M)', max_length=1)
    age = models.IntegerField('Age', max_length=2)
    brief_info = models.TextField('Background Infomation', default="")

    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

class ShareFood(models.Model):
    location_name = models.TextField('Location Name', default="")
    location = models.TextField('Location', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time',auto_now=True)
    participants = models.ManyToManyField(Info)
    num_people = models.IntegerField("Number of people", default=2)
    host = models.CharField("Host's Name", default="", max_length=30)
    full = models.BooleanField(default=False)

    def get_location(self):
        return f"Meeting Location : {self.location}"

    def get_time(self):
        return f"Time to meet up with other participants : {str(self.date_time)}"

    def full_or_not(self):
        if len(self.participants.all()) == self.num_people:
            self.full = True
            self.save()
        return len(self.participants.all()) == self.num_people

    

class ShareRide(models.Model):
    myDate = datetime.now()
    formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

    location_name = models.TextField('Location Name', default="")
    location = models.TextField('Location', default="")
    destination_name = models.TextField('Destination Name', default="")
    destination = models.TextField('Destination', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time', default=formatedDate)
    participants = models.ManyToManyField(Info)
    num_people = models.IntegerField("Number of people", default=2)
    host = models.CharField("Host's Name", default="", max_length=30)
    full = models.BooleanField(default=False)

    def get_destination_name(self):
        return f"Destination : {self.destination_name}"

    def get_destination(self):
        return f"Destination Address : {self.destination}"

    def get_location_name(self):
        return f"Meeting Location : {self.location_name}"

    def get_location(self):
        return f"Address : {self.location}"

    def get_time(self):
        return f"Time to meet up with other participants : {str(self.date_time)}"

    def full_or_not(self):
        if len(self.participants.all()) == self.num_people:
            self.full = True
            self.save()
        return len(self.participants.all()) == self.num_people

    def del_self(self):
        share = self
        self.delete()
        self.save()

class SharePromotion(models.Model):
    location_name = models.TextField('Location Name', default="")
    location = models.TextField('Location', default="")
    brand = models.TextField('Brand', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time')
    participants = models.ManyToManyField(Info)
    num_people = models.IntegerField("Number of people", default=2)
    host = models.CharField("Host's Name", default="", max_length=30)
    full = models.BooleanField(default=False)

    def get_location(self):
        return f"Meeting Location : {self.location}"

    def get_brand(self):
        return f"Name of Store or Brand : {self.brand}"

    def get_description(self):
        return f"Brief description : {self.description}"

    def get_time(self):
        return f"Time to meet up with other participants : {str(self.date_time)}"

    def full_or_not(self):
        if len(self.participants.all()) == self.num_people:
            self.full = True
            self.save()
        return len(self.participants.all()) == self.num_people
