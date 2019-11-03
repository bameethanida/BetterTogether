from django.db import models

class User(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    gender = models.CharField('Gender', max_length=1)
    date_time = models.DateTimeField('Date and Time')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

