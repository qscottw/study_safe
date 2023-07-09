from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from datetime import date
# Create your models here.
class Venue(models.Model):
    class VenueType(models.TextChoices):
        LECTURE_THEATRE = 'LT', _('Lecture Theatre')
        CLASSROOM = 'CR', _('Classroom')
        TUTORIAL_ROOM = 'TR', _('Tutorial Room')
    id = models.AutoField(primary_key=True)
    venue_code=models.CharField(max_length=20)
    location=models.CharField(max_length=150)
    type=models.CharField(
        max_length=2,
        choices=VenueType.choices
    )
    capacity=models.IntegerField()
    def __str__(self):
        return self.venue_code

class HKUMember(models.Model):
    hku_id=models.CharField(primary_key=True, max_length=10)
    name=models.CharField(max_length=150)
    # diagnoseDate=models.DateField(default=now)
    def __str__(self):
        return self.name

class Record(models.Model):
    # need to make sure that leave is larger than enter
    class EventType(models.TextChoices):
        ENTRY = 'Entry', _('Entry - Event')
        EXIT = 'Exit', _('Exit - Event')
    dateTime=models.DateTimeField()
    event=models.CharField(
        max_length=5,
        choices=EventType.choices,
    )
    venue=models.ForeignKey(Venue, on_delete=models.CASCADE)
    member=models.ForeignKey(HKUMember, on_delete=models.CASCADE)

    def __str__(self):
        return "By "+self.member.name+" from "+self.dateTime.strftime("%Y/%m/%dT%H:%M:%S")


class User(models.Model):
    username=models.CharField(unique=True, max_length=20)
    password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20, null=True, blank=True)
    last_name=models.CharField(max_length=20, null=True, blank=True)
    email=models.CharField(max_length=40, null=True, blank=True)
    def __str__(self):
        return f"{self.username} - {self.first_name}"