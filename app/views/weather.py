import requests
from django.shortcuts import render
from django.views import View
from django.conf import settings
from rest_framework.generics import GenericAPIView

from app.models import WeatherQuery
from app.serializers import WeatherSerializer
from rest_framework import generics


class WeatherAPIView(GenericAPIView):
    def get(self, request):
        history = WeatherQuery.objects.all().order_by('-timestamp')[:10]
        return render(request, 'index.html', {'history': history})

    def post(self, request):
        city_name = request.POST.get('city')
        api_key = settings.WEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city_name': city_name,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }

            WeatherQuery.objects.create(**weather_data)

            return render(request, 'index.html', {
                'weather': weather_data,
                'history': WeatherQuery.objects.all().order_by('-timestamp')[:10]
            })
        else:
            return render(request, 'index.html', {
                'error': 'Город не найден',
                'history': WeatherQuery.objects.all().order_by('-timestamp')[:10]
            })


class WeatherQueryHistoryView(View):
    def get(self, request):
        history = WeatherQuery.objects.all().order_by('-timestamp')
        return render(request, 'history.html', {'history': history})


class WeatherQueryListCreateAPIView(generics.ListCreateAPIView):
    queryset = WeatherQuery.objects.all().order_by('-timestamp')
    serializer_class = WeatherSerializer


class WeatherQueryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = WeatherQuery.objects.all()
    serializer_class = WeatherSerializer