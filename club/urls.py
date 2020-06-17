from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resources/', views.getResources, name='resources'),
    path('meetings/', views.getMeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingDetails, name='meetingdetails'),
    path('newresource/', views.newResource, name='newresource'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('loginmsg/', views.loginmsg, name='loginmsg'),
    path('logoutmsg/', views.logoutmsg, name='logoutmsg')
]