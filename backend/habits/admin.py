from django.contrib import admin
from .models import Habit, HabitFrequency, HabitPeriod, HabitRecord, HabitTimer, User, Workspace

# Register your models here.

admin.site.register(Habit)
admin.site.register(HabitFrequency)
admin.site.register(HabitPeriod)
admin.site.register(HabitRecord)
admin.site.register(HabitTimer)
admin.site.register(User)
admin.site.register(Workspace)
