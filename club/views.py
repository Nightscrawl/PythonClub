from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm

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


@login_required
def newResource(request):
    form = ResourceForm
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})


@login_required
def newMeeting(request):
    form = MeetingForm
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})


def loginmsg(request):
    return render(request, 'club/loginmsg.html')

def logoutmsg(request):
    return render(request, 'club/logoutmsg.html')
