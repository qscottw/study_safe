from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('venue/', venue_view),
    path('contact/', contact_view)
]
