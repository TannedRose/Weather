from django.db import models
from django.utils import timezone

class WeatherQuery(models.Model):
    city_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()

    def __str__(self):
        return f"{self.city_name} в {self.timestamp}"
