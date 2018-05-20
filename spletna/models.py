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

class Interest(models.Model):

	#user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)
	value = models.FloatField(default = 0.0)

class UserProfile(models.Model):
	#user = models.OneToOneField(User, on_delete= models.CASCADE)
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	interests_calc = models.CharField(max_length = 60000)
	profile_image = models.ImageField(upload_to='', blank=True, null=True)
	interests = models.ManyToManyField(Interest, related_name="interests")
	#interests_calc = models.ManyToManyField(Interest, related_name="interests_calc", blank = True)
	


class Meeting(models.Model):
	
	location = models.ForeignKey(Location, on_delete= models.CASCADE)
	timestamp = models.DateTimeField()
	users = models.ManyToManyField(UserProfile)



'''class UserHobby(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete= models.SET_NULL)
	hobbies = models.ManyToManyField(Hobby)

'''