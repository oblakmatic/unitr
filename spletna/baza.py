from .models import *
from django.db import models
from django.contrib.auth.models import User
import datetime


def baza(neki):

    user1 = User.objects.create_user('John', 'lennon@thebeatles.com', 'johnpassword')
    user1.last_name = "Lennon"

    user2 = User.objects.create_user('Anja', 'anja@thebeatles.com', 'adminadmin')
    user2.last_name = "Zupancic"
    '''
        user2 = User.objects.create_user('Tomaž', 'tomaž@thebeatles.com', 'adminadmin')
        user2.last_name = "Klemenčič"

        user2 = User.objects.create_user('Jure', 'jure@thebeatles.com', 'adminadmin')
        user2.last_name = "Horvat"

        user2 = User.objects.create_user('Ana', 'ana@thebeatles.com', 'adminadmin')
        user2.last_name = "Jurean"

        user2 = User.objects.create_user('Eva', 'eva@thebeatles.com', 'adminadmin')
        user2.last_name = "Oman"

        user2 = User.objects.create_user('Klemen', 'klemen@thebeatles.com', 'adminadmin')
        user2.last_name = "Kukic"

        user2 = User.objects.create_user('Sara', 'sara@thebeatles.com', 'adminadmin')
        user2.last_name = "Ferbežar"

        user2 = User.objects.create_user('Sonja', 'sonja@thebeatles.com', 'adminadmin')
        user2.last_name = "Juric"'''
        
    userprof3 = UserProfile(username="anjaz", name ="Anja Zupančič")
    userprof3.save()

    userprof4 = UserProfile(username="jureh", name ="Jure Horvat")
    userprof4.save()

    
    
    userprof = UserProfile(username="jozeg", name ="Jože Gorišek")
    userprof.save()

    userprof = UserProfile(username="tomazk", name ="Tomaž Klemenčič")
    userprof.save()

    

    userprof = UserProfile(username="evao", name ="Eva Oman")
    userprof.save()

    userprof9 = UserProfile(username="klemenk", name ="Klemen Kukic")
    userprof9.save()

    userprof7 = UserProfile(username="saraf", name ="Sara Ferbežar")
    userprof7.save()


    lokacija = Location(name="Špica", longitude=14.5729099,latitude=45.9839161, address = "Kočevska cesta 1, 1290 Škofljica")
    lokacija.save()

    lokacija3 = Location(name="KantinaMeksikana", longitude=14.5033773,latitude=46.0512596, address = "Wolfova ulica 2, 1000 Ljubljana")
    lokacija3.save()

    lokacija2 = Location(name="Aeroklub Havana", longitude=14.5250023,latitude=46.101553, address = "Dunajska cesta 342, 1031 Črnuče")
    lokacija2.save()

    lokacija = Location(name="Bowling klub 300", longitude=14.5250023,latitude=46.101553, address = "Rengentova cesta 130 , 1000 Ljubljana")
    lokacija.save()




    userprof = UserProfile(username="thelegend27", name ="Jože Gorišek")
    userprof.save()
    userprof2 = UserProfile(username="dragonslayer", name ="Matic Oblak")
    userprof2.save()

    inte = Interest(name="Rugby", value = 0.12)
    inte.save()
    inte2 = Interest(name="Sailing", value = 0.12)
    inte2.save()
    inte3 = Interest(name="Polo", value = 0.12)
    inte3.save()
    inte4 = Interest(name="Skiing", value = 0.12)
    inte4.save()
    inte5 = Interest(name="Travel", value = 0.12)
    inte5.save()

    userprof2.interests.add(inte)
    userprof2.interests.add(inte2)
    userprof2.interests.add(inte3)

    userprof3.interests.add(inte)
    userprof3.interests.add(inte2)
    userprof3.interests.add(inte3)

    userprof9.interests.add(inte)
    userprof9.interests.add(inte4)
    userprof9.interests.add(inte3)

    userprof.interests.add(inte)
    userprof.interests.add(inte4)
    userprof.interests.add(inte5)

    userprof7.interests.add(inte4)
    userprof7.interests.add(inte2)
    userprof7.interests.add(inte3)
    
    meeting = Meeting(location = lokacija, timestamp = "2018-05-20T19:00:00")
    meeting.save()

    meeting.users.add(userprof3)
    meeting.users.add(userprof2)
    meeting.users.add(userprof)

    meeting = Meeting(location = lokacija, timestamp = "2018-04-30T18:00:00")
    meeting.save()

    meeting.users.add(userprof)
    meeting.users.add(userprof3)
    meeting.users.add(userprof9)

    meeting = Meeting(location = lokacija, timestamp = "2018-05-10T20:00:00")
    meeting.save()

    meeting.users.add(userprof7)
    meeting.users.add(userprof3)
    meeting.users.add(userprof)