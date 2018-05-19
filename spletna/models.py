from django.db import models
from django.contrib.auth.models import User
import os

class Hobby(models.Model):
    name = models.CharField(max_length = 30)

class Location(models.Model):
	name = models.CharField(max_length=50)
	longitude = models.FloatField()
	latitude = models.FloatField()
	address = models.CharField(max_length=100)

class Meeting(models.Model):
	time = models.DateTimeField()
	location = models.ForeignKey(Location, on_delete= models.CASCADE)
	user = models.ManyToManyField(User)



class UserHobby(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete= models.SET_NULL)
	hobbies = models.ManyToManyField(Hobby)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	profile_image = models.ImageField(upload_to='', blank=True, null=True)