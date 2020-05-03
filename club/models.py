from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda -- DONE

class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField(auto_now=False)
    meetingLocation=models.CharField(max_length=255)
    meetingAgenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingTitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'


# Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text -- DONE

class MeetingMinutes(models.Model):
    meetingMinutesID=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingMinutesAttendance=models.ManyToManyField(User)
    meetingMinutesText=models.TextField()

    def __str__(self):
        return self.meeting


# Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description -- DONE

class Resource(models.Model):
    resourceUserID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    resourceUrl=models.URLField(null=True, blank=True)
    resourceDateEntered=models.DateField()
    resourceDescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'


# Event which will have fields for event title, location, date, time, description and the user id of the member that posted it -- DONE

class Event(models.Model):
    eventUserID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    eventTitle=models.CharField(max_length=255)
    eventLocation=models.CharField(max_length=255)
    eventDate=models.DateField()
    eventTime=models.TimeField(auto_now=False)
    eventDescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table='event'
        verbose_name_plural='events'
