from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('resources/',views.resources),
    path('resourcegroups/',views.resourcegroups),
    path('heros/',views.heros),
]