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

class UserProfile(models.Model):
	#user = models.OneToOneField(User, on_delete= models.CASCADE)
	name = models.CharField(max_length=100)
	profile_image = models.ImageField(upload_to='', blank=True, null=True)
	
class Meeting(models.Model):
	
	location = models.ForeignKey(Location, on_delete= models.CASCADE)
	timestamp = models.DateTimeField()
	users = models.ManyToManyField(UserProfile)



class UserHobby(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete= models.SET_NULL)
	hobbies = models.ManyToManyField(Hobby)

