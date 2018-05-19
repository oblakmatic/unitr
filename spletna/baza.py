from .models import *
from django.db import models
from django.contrib.auth.models import User
import datetime


def baza(neki):

    user1 = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user1.last_name = "lennon"

    user2 = User.objects.create_user('anja', 'anja@thebeatles.com', 'adminadmin')
    user2.last_name = "Zupancic"

    lokacija = Location(name="Spica", longitude=50.1,latitude=66.1, address = "Trubajeva ulica 2")
    lokacija.save()

    lokacija = Location(name="Union", longitude=1.1,latitude=36.1, address = "Verjameva ulica 2")
    lokacija.save()

    meeting = Meeting(location = lokacija, time = datetime.date.today())
    meeting.save()

    meeting.user.add(user1)
    meeting.user.add(user2)
