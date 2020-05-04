from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def getResources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list' : resource_list})

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list' : meeting_list})

def meetingDetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)  # don't forget the model name here!!
    # discount=prod.memberdiscount
    # reviews=Review.objects.filter(product=id).count()
    context={
        'meeting' : meeting,
        # 'discount' : discount,
        # 'reviews' : reviews,
    }
    return render(request, 'club/meetingdetails.html', context=context)
