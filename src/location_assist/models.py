from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# class Person(models.Model):
# 	userName = models.ForeignKey(user.username)
# 	firstName = models.

class SaveSettings(models.Model):
    longitude = models.DecimalField(max_digits = 9, decimal_places = 8)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 8)
    volume = models.IntegerField()
    username = models.ForeignKey(User, null = True)
    activity = models.TextField(null = True)

    def __str__(self):
    	location = str(self.latitude) +"_" + str(self.longitude)
        return location

