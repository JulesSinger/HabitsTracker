from django.urls import path
from habitsApi import views

urlpatterns = [
    path('habits/', views.habitApi),
    path('habits/<int:pk>/', views.habitApi),
] 