from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from habitsApi.serializers import *
from habitsApi import *

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