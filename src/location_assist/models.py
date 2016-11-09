from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# class Person(models.Model):
# 	userName = models.ForeignKey(user.username)
# 	firstName = models.

class SaveSettings(models.Model):
    longitude = models.DecimalField(max_digits = 10, decimal_places = 8)
    latitude = models.DecimalField(max_digits = 10, decimal_places = 8)
    volumeLevel = models.FloatField(null = True)
    vibrationMode = models.BooleanField(default = False)
    brightness = models.FloatField(null =True)
    mobileData = models.BooleanField(default = False)
    wifi = models.BooleanField(default = False)
    bluetooth = models.BooleanField(default = False) 
    username = models.ForeignKey(User, null = True)
    activity = models.TextField(null = True, blank = True)

    def __str__(self):
    	location = "_" + str(self.latitude) +"_" + str(self.longitude)
        return location

class Live(models.Model):
    longitude = models.DecimalField(max_digits = 10, decimal_places = 8)
    latitude = models.DecimalField(max_digits = 10, decimal_places = 8)
    time = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User)

    def __str__(self):
    	return self.username

class Reminder(models.Model):
    longitude = models.DecimalField(max_digits = 10, decimal_places = 8)
    latitude = models.DecimalField(max_digits = 10, decimal_places = 8)
    username = models.ForeignKey(User)
    reminder_title = models.CharField(max_length = 100)
    reminder_text = models.TextField(null = True)

    def __str__(self):
        namevalue =  str(self.username) + "_" + str(self.longitude) + "_" + str(self.latitude)
        return namevalue