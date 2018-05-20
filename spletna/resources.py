from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import *
from tastypie.authorization import *
from tastypie import fields
import numpy as np

import csv
from recommender_system import *

recommender = Recommender()

hobbies = {}
with open('recommender_data/hobbies.dat', 'r', encoding="utf8") as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            for row in reader:
                hobbies[row[1]] = row[0]
                #a = Interest(name=row[])
            #print("len(hobbies): ", len(hobbies))

#print(hobbies)
class LocationResource(ModelResource):

    
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        authorization = Authorization()
        include_resource_uri = False

class InterestResource(ModelResource):
    class Meta:
        queryset = Interest.objects.all()
        resource_name = 'interest'
        authorization = Authorization()
        excludes = ['id']
        include_resource_uri = False

class UserResource(ModelResource):

    interest = fields.ToManyField(InterestResource,'interests',full=True)
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        include_resource_uri = False
        filtering = {   
            'username' : ALL,
        }

    def hydrate(self, bundle):
        # Don't change existing slugs.
        # In reality, this would be better implemented at the ``Note.save``
        # level, but is for demonstration.
        #print("nriwa")
        zanimanja = bundle.data["interest"]
        #print(bundle)
        if bundle.data["id"]:
            userIdx = bundle.data["id"]
            new_user_data = np.array([(int(userIdx), int(hobbies[zanimanje["name"]]), float(zanimanje["value"])) for zanimanje in zanimanja])
            all_hobbies = recommender.get_all_hobbies(new_user_data)
            awt = np.array2string(all_hobbies)
            #print(awt)
            #print("fawi")
            #uporabnik = UserProfile.objects.get(id=userIdx)
            #uporabnik.interests_calc = awt
            #uporabnik.save()
            bundle.data["interests_calc"] = awt
        

        return bundle

class MeetingResource(ModelResource):
    #name = fields.ForeignKey(Location, full=True, attribute='name')
    #category = fields.ForeignKey(ExpenseCategoryResource, attribute='category', null=True, full=True)
    location = fields.ForeignKey(LocationResource, 'location', full = True)
    users = fields.ToManyField(UserResource,'users',full=True, null=True, blank=True)
    #users = fields.ListField()
    
    #def dehydrate_users(self,bundle):
    #    return bundle.obj.users.all().values()

    class Meta:
        queryset = Meeting.objects.all()
        resource_name = 'meeting'
        authorization = Authorization()
        include_resource_uri = False
        filtering = {
            'user': ALL_WITH_RELATIONS
        }

