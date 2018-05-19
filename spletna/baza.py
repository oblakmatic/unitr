from .models import *
from django.db import models
from django.contrib.auth.models import User


def baza(neki):

    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.last_name = "lennon"

    user = User.objects.create_user('anja', 'anja@thebeatles.com', 'adminadmin')
    user.last_name = "Zupancic"

    lokacija = Location(name="Spica", longitude=50.1,latitude=66.1, address = "Trubajeva ulica 2")
    lokacija.save()

    lokacija = Location(name="Union", longitude=1.1,latitude=36.1, address = "Verjameva ulica 2")
    lokacija.save()

    