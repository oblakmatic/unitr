from django.conf.urls import url, include
from rest_framework import routers
from spletna import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from spletna.resources import *
from tastypie.api import Api

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'userprofiles', views.UserProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


location_resource = LocationResource()
meeting_resource = MeetingResource()

v1_api = Api(api_name='v1')
v1_api.register(LocationResource())
v1_api.register(MeetingResource())
v1_api.register(UserResource())

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'api/', include(v1_api.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)