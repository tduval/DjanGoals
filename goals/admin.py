from django.contrib import admin
from .models import Goal, Track

# Register your models here.


class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_text', 'owner', 'tracks_count', 'start_date', 'end_date', 'tracks_mean')

    def tracks_count(self, obj):
        return obj.track_set.count()

    def tracks_mean(self, obj):
        tracks = obj.track_set.all()
        if tracks.count() == 0:
            return 0
        else:
            mean = 0
            for t in tracks:
                mean += t.track_score
            return mean/(self.tracks_count(obj))


class TrackAdmin(admin.ModelAdmin):
    list_display = ('date', 'goal', 'track_score', 'comment_text')

admin.site.register(Goal, GoalAdmin)
admin.site.register(Track, TrackAdmin)

