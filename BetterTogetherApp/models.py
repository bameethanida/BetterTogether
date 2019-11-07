from django.db import models
from django import forms
from django.contrib.auth.models import User
import datetime

class Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField('Gender (F or M)', max_length=1)
    age = models.IntegerField('Age', max_length=2)

    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

class ShareFood(models.Model):
    location = models.TextField('Location', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time')
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
    location = models.TextField('Location', default="")
    destination = models.TextField('Destination', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time')
    participants = models.ManyToManyField(Info)
    num_people = models.IntegerField("Number of people", default=2)
    host = models.CharField("Host's Name", default="", max_length=30)
    full = models.BooleanField(default=False)

    def get_destination(self):
        return f"Destination : {self.destination}"

    def get_location(self):
        return f"Meeting Location : {self.location}"

    def get_time(self):
        return f"Time to meet up with other participants : {str(self.date_time)}"

    def full_or_not(self):
        if len(self.participants.all()) == self.num_people:
            self.full = True
            self.save()
        return len(self.participants.all()) == self.num_people

class SharePromotion(models.Model):
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

    def get_time(self):
        return f"Time to meet up with other participants : {str(self.date_time)}"

    def full_or_not(self):
        if len(self.participants.all()) == self.num_people:
            self.full = True
            self.save()
        return len(self.participants.all()) == self.num_people

class DateForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
    time = forms.TimeField(initial=datetime.time)
