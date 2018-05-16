from django.contrib import admin

from .models import Goal, Track

# Register your models here.

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_text', 'owner', 'tracks_count', 'start_date', 'end_date')

    def tracks_count(self, obj):
        return obj.track_set.count()



admin.site.register(Goal, GoalAdmin)
admin.site.register(Track)

