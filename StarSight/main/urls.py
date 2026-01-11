from django.urls import path
from . import views
from dairy import views as dairy_views

urlpatterns = [
    path('', views.index, name='home'),
    path('heatmap/', views.weather_check, name='weather_check')
]