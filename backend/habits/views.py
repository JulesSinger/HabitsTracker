from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from habits.serializers import *
from habits import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

def index(request):
    habits = Habit.objects.all()
    return HttpResponse(habits)

def detail(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    return HttpResponse(habit)

def create(request):
    print(request)
    habit_data = request.POST
    habit = Habit(title=habit_data['title'], color=habit_data['color'])
    habit.save()
    return JsonResponse("Habitude créée avec succès.", safe=False)
    

def records(request, habit_id):
    return HttpResponse("You're looking at the records of habit %s." % habit_id)

@csrf_exempt
def habitApi(request,id=0):
    # GET request for all habits
    if request.method == 'GET':
        habits = Habit.objects.all()
        habits_serializer = HabitSerializer(habits, many=True)
        return JsonResponse(habits_serializer.data, safe=False)
    # POST request to add an habit
    elif request.method=='POST':
        habit_data = JSONParser().parse(request)
        habits_serializer = HabitSerializer(data=habit_data)
        if habits_serializer.is_valid():
            habits_serializer.save()
            return JsonResponse("Habitude créée avec succès.", safe=False)
        return JsonResponse("Erreur lors de la création de l'habitude.",safe=False)
    elif request.method == 'PUT':
        habit_data = JSONParser().parse(request)
        habit = Habit.objects.get(id=id)
        habits_serializer = HabitSerializer(habit,data=habit_data)
        if habits_serializer.is_valid():
            habits_serializer.save()
            return JsonResponse("Habitude mis à jour avec succès.",safe=False)
        return JsonResponse("Erreur lors de la mis à jour de l'habitude.")
    elif request.method=='DELETE':
        habit = Habit.objects.get(id=id)
        habit.delete()
        return JsonResponse("Habitude supprimée avec succès.",safe=False)