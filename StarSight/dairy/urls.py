from django.urls import path
from . import  views

urlpatterns = [
    path('', views.observations_list, name='observations_list'),
    path('add/', views.add_observation, name='add_observation')
]