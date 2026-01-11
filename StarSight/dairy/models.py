from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CelestialBody(models.Model):
    name = models.CharField(max_length=100)
    body_type = models.CharField(max_length=50, blank=True)  # Луна, звезда, планета и т.д.
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Observation(models.Model):
    date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="observations/", blank=True, null=True)

    # Один прибор на запись
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)

    # Одно небесное тело на запись
    celestial_body = models.ForeignKey(CelestialBody, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
