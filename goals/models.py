from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_text = models.CharField(max_length=50)
    description_text = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.goal_text

class Track(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    date = models.DateField('date')
    track_score = models.IntegerField(default=0)
    comment_text = models.CharField(max_length=255)

    def __str__(self):
        return self.date
