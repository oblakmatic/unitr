from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from .models import *
from tastypie.authorization import *
from tastypie import fields


class LocationResource(ModelResource):

    
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        authorization = Authorization()

class UserResource(ModelResource):

    
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'users'
        authorization = Authorization()
        filtering = {
            'name' : ALL,
        }

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

    