from django.urls import path

from . import views

app_name = 'goals'
urlpatterns = [
    #ex: /goals
    path('', views.index, name='index'),
    #ex: /goals/5/
    path('<int:goal_id>/', views.goal, name='goal'),
    #ex: /goals/5/tracks
    path('<int:goal_id>/tracks/', views.tracks, name='tracks'),
]
