from django.db import models

class User(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    gender = models.CharField('Gender (F or M)', max_length=1)
    age = models.IntegerField('Age', max_length=2)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

class ShareFood(models.Model):
    location = models.TextField('Location', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time')
    user = models.ManyToManyField(User)
    host = models.CharField("Host's Name", default="", max_length=30)

class ShareRide(models.Model):
    location = models.TextField('Location', default="")
    destination = models.TextField('Destination', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time')
    user = models.ManyToManyField(User)
    host = models.CharField("Host's Name", default="", max_length=30)

    def get_location(self):
        return f"Location : {self.location}"

    def get_destination(self):
        return f"Destination : {self.destination}"

class SharePromotion(models.Model):
    location = models.TextField('Location', default="")
    brand = models.TextField('Brand', default="")
    description = models.TextField('Description', default="")
    date_time = models.DateTimeField('Date and Time')
    user = models.ManyToManyField(User)
    host = models.CharField("Host's Name", default="", max_length=30)


