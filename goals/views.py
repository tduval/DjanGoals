from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Goal
from .models import Track

# index pages/default page displayed all Goals
@login_required(login_url='/accounts/login/')
def index(request):
    goal_list = Goal.objects.filter(owner=request.user)
    return render(request, 'goals/index.html', {'goal_list': goal_list})

# Checks if the authenticvated user try to access their own goals and not someone else goals page
# detail page of a specific goal with all his associated Tracks
@login_required(login_url='/accounts/login/')
def goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    if not goal.owner == request.user:
        return redirect('goals:index')
    track_list = Track.objects.filter(goal=goal_id)
    return render(request, 'goals/goal.html', {'goal': goal, 'track_list': track_list})

# Post form to create a new tracks from a specific goal
@login_required(login_url='/accounts/login/')
def tracks(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    track = Track(goal=goal, date=datetime.date.today())
    track.track_score = request.POST['score']
    track.comment_text = request.POST['comment']
    track.save()
    return HttpResponseRedirect(reverse('goals:goal', args=(goal.id,)))

