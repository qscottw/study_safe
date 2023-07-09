from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Venue)
admin.site.register(HKUMember)
admin.site.register(Record)
admin.site.register(User)