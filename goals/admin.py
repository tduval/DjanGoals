from django.contrib import admin

from .models import Goal, Track

# Register your models here.

class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_text', 'owner', 'start_date', 'end_date')

admin.site.register(Goal, GoalAdmin)
admin.site.register(Track)

