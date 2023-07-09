from django.urls import path, include
from .api_views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r'venues', VenueViewSet, 'venue')
router.register(r'records', RecordViewSet, 'record')
router.register(r'members', MemberViewSet, 'member')
urlpatterns=[
    path('api/venues_visited/', get_venues_visited),
    path('api/close_contacts/', get_close_contacts),
    path('api/', include(router.urls)),
]
# print(router.urls)

# urlpatterns.extend([
#     path('api/venues/<str:venue_code>', VenueViewSet.as_view({"get":"retrieve", "put": "update", "delete": "destroy"}))
# ])