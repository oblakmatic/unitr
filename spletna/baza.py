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



    userprof = UserProfile(username="thelegend27", name ="Jože Gorišek")
    userprof.save()
    userprof2 = UserProfile(username="dragonslayer", name ="Matic Oblak")
    userprof2.save()


    inte = Interest( name="Swimming", value = 0.52)
    inte.save()
    userprof.interests.add(inte)
    inte = Interest(name="Cooking", value = 0.22)
    inte.save()
    userprof.interests.add(inte)
    inte = Interest( name="Driving", value = 0.82)
    inte.save()
    userprof.interests.add(inte)
    inte = Interest(name="Driving", value = 0.12)
    inte.save()
    userprof2.interests.add(inte)
    
    meeting = Meeting(location = lokacija, timestamp = datetime.date.today())
    
    meeting.save()
    meeting.users.add(userprof)

