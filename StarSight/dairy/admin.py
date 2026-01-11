from django.contrib import admin
from .models import Observation, Equipment, CelestialBody

admin.site.register(Observation)
admin.site.register(Equipment)
admin.site.register(CelestialBody)
