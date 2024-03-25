from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
# Workspace model
class Workspace(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workspaces')

    def __str__(self):
        return self.name
    
# HabitPeriod model
class HabitPeriod(models.Model):
    title = models.DateField()
    
# HabitFrequency model
class HabitFrequency(models.Model):
    periodicity = models.CharField(max_length=100)
    number_of_days = models.IntegerField()
    
    def __str__(self):
        return self.periodicity + ' - ' + str(self.number_of_days) + ' days'

# HabitTimer model
class HabitTimer(models.Model):
    time_min = models.IntegerField()
    
    def __str__(self):
        return str(self.time_min) + ' minutes'

# Habit model
class Habit(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    period = models.ForeignKey(HabitPeriod, on_delete=models.CASCADE, related_name='habits')
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='habits')
    frequency = models.ForeignKey(HabitFrequency, on_delete=models.CASCADE, related_name='habits')
    timer = models.ForeignKey(HabitTimer, on_delete=models.CASCADE, related_name='habits')

    def __str__(self):
        return self.name
    
# HabitRecord model
class HabitRecord(models.Model):
    date = models.DateField()
    done = models.BooleanField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='records')

    def __str__(self):
        return self.date + ' - ' + self.habit.title + ' - ' + str(self.done)
    
# ConfigPeriod model
class ConfigPeriod(models.Model):
    daily = models.IntegerField()
    weekly = models.IntegerField()
    monthly = models.IntegerField()
    yearly = models.IntegerField()
    
    def __str__(self):
        return 'Daily: ' + str(self.daily) + ' - Weekly: ' + str(self.weekly) + ' - Monthly: ' + str(self.monthly) + ' - Yearly: ' + str(self.yearly)