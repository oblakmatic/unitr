from tastypie.resources import ModelResource
from .models import *
from tastypie.authorization import *

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        authorization = Authorization()

class MeetingResource(ModelResource):
    class Meta:
        queryset = Meeting.objects.all()
        resource_name = 'meeting'
        authorization = Authorization()