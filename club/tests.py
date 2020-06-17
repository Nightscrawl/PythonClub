from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getResources, getMeetings, meetingDetails
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class MeetingTest(TestCase):
    def setup(self):
        type = Meeting(meetingTitle = "Phantom Meeting")
        meeting = Meeting(meetingTitle = type, meetingDate = "2020-05-31", meetingTime = "14:00:00", meetingLocation = "Room 3", meetingAgenda = "meeting agenda placeholder")
        return meeting

    def test_type(self):
        meeting = self.setup()
        self.assertEqual(str(meeting.meetingTitle), "Phantom Meeting")

    def test_string(self):
        meeting = self.setup()
        self.assertEqual(str(meeting.meetingAgenda), "meeting agenda placeholder")
        # self.assertEqual(str(meeting.meetingAgenda), "Discuss web traffic.")   # uncomment to see test failure

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), "meeting")


class MeetingMinutesTest(TestCase):
    def setup(self):
        # self.u = User.objects.create(username = "snake_usr")
        type = Meeting(meetingTitle = "Phantom Meeting")
        # mins = MeetingMinutes.objects.create(meetingMinutesID = type, meetingMinutesAttendance = self.u, meetingMinutesText = "minutes placeholder")
        # mins.user.add(self.u)
        mins = MeetingMinutes(meetingMinutesID = type, meetingMinutesText = "minutes placeholder")
        return mins

            # i tried many things but could not get the many to many relationship to work with meetingMinutesAttendance
            # ideally, for my purposes, i would be able to assign many users to the meeting minutes -- all the users that attended the meeting

    def test_string(self):
        mins = self.setup()
        self.assertEqual(str(mins.meetingMinutesText), "minutes placeholder")

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), "club_meetingminutes")


class ResourceTest(TestCase):
    def setup(self):
        type = Resource(resourceType = "website")
        res = Resource(resourceName = "Python and You", resourceType = type, resourceUrl = "https://www.pay.com", resourceDateEntered = "2020-04-01", resourceDescription = "resource description placeholder")
        return res

    def test_string(self):
        res = self.setup()
        self.assertEqual(str(res.resourceName), "Python and You")

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), "resource")


class EventTest(TestCase):
    def setup(self):
        type = Event(eventTitle = "Snake-themed costume party")
        evt = Event(eventTitle = type, eventLocation = "Python Party Place", eventDate = "2020-04-01", eventTime = "14:00:00", eventDescription = "event description placeholder")
        return evt

    def test_string(self):
        evt = self.setup()
        self.assertEqual(str(evt.eventTitle), "Snake-themed costume party")

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), "event")


# testing basic views ----------

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
  
class GetMeetingsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse("meetings"))
       self.assertEqual(response.status_code, 200)

class GetResourcesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("resources"))
        self.assertEqual(response.status_code, 200)



class New_Resource_authentication_test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="testuser1", password="P@ssw0rd1")
        self.res = Resource.objects.create(resourceUserID = self.test_user, resourceName = "Python and You", resourceType = "website", resourceUrl = "https://www.pay.com", resourceDateEntered = "2019-04-02", resourceDescription = "resource description placeholder")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse("newresource"))
        self.assertRedirects(response, "/accounts/login/?next=/club/newresource/")

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username="testuser1", password="P@ssw0rd1")
        response=self.client.get(reverse("newresource"))
        self.assertEqual(str(response.context["user"]), "testuser1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "club/newresource.html")
