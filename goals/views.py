from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import Goal
from .models import Track

# index pages/default page displayed all Goals
@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'GET':
        goal_list = Goal.objects.filter(owner=request.user)
        return render(request, 'goals/index.html', {'goal_list': goal_list})
    elif request.method == 'POST':
        goal = Goal.objects.create(owner=request.user, goal_text=request.POST.get("AddGoal"), description_text="", start_date=datetime.date.today(), end_date=datetime.date.today().replace(year=9999))
        return redirect('goals:index')

# detail page of a specific goal with all his associated Tracks
@login_required(login_url='/accounts/login/')
def goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    if not goal.owner == request.user:
        # Checks if the authenticvated user try to access their own goals and not someone else goals page
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


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
