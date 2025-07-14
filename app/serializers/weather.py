from rest_framework import serializers
from app.models import WeatherQuery


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherQuery
        fields = '__all__'