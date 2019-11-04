from django.db import models

class User(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    gender = models.CharField('Gender', max_length=1)
    age = models.IntegerField('Age', max_length=2)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

class ShareFood(models.Model):
    location = models.TextField('Location', blank=False)
    description = models.TextField('Description', blank=False)
    date_time = models.DateTimeField('Date and Time')
    user = models.ManyToManyField(User)
    host = models.TextField("Host's Name", blank=False)

class ShareRide(models.Model):
    location = models.TextField('Location', blank=False)
    destination = models.TextField('Destination', blank=False)
    description = models.TextField('Description', blank=False)
    date_time = models.DateTimeField('Date and Time')
    user = models.ManyToManyField(User)
    host = models.TextField("Host's Name", blank=False)

class SharePromotion(models.Model):
    location = models.TextField('Location', blank=False)
    brand = models.TextField('Brand', blank=False)
    description = models.TextField('Description', blank=False)
    date_time = models.DateTimeField('Date and Time')
    user = models.ManyToManyField(User)
    host = models.TextField("Host's Name", blank=False)


