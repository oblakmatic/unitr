from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Hobby)
admin.site.register(Meeting)