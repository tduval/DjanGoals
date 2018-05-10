from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.urls import reverse
from .models import Goal
from .models import Track

# index pages/default page displayed all Goals
def index(request):
    goal_list = Goal.objects.all()
    return render(request, 'goals/index.html', {'goal_list': goal_list})

# detail page of a specific goal with all his associated Tracks
def goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    track_list = Track.objects.filter(goal=goal_id)
    return render(request, 'goals/goal.html', {'goal': goal, 'track_list': track_list})

# Post form to create a new tracks from a specific goal
def tracks(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    track = Track(goal=goal, date=datetime.date.today())
    track.track_score = request.POST['score']
    track.comment_text = request.POST['comment']
    track.save()
    return HttpResponseRedirect(reverse('goals:goal', args=(goal.id,)))

