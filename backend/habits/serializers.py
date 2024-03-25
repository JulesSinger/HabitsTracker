from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

class WorkspaceSerializer(serializers.ModelSerializer):
    habits = HabitSerializer(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'color', 'user', 'habits']

class HabitPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitPeriod
        fields = '__all__'

class HabitFrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitFrequency
        fields = '__all__'

class HabitTimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitTimer
        fields = '__all__'

class HabitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitRecord
        fields = '__all__'

class ConfigPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigPeriod
        fields = '__all__'