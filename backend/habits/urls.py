from django.urls import path

from . import views

app_name = "habits"

urlpatterns = [
  path("", views.index, name="index"),
  path('<int:pk>', views.detail, name="detail"),
  #path('<int:pk>/records', views.ResultsView.as_view(), name="records"),
  path("create", views.create, name="create"),
]