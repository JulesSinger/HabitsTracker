from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('habits/', include("habits.urls")),
    path("admin/", admin.site.urls),
] 