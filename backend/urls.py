"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import WeatherAPIView, WeatherQueryHistoryView, WeatherQueryRetrieveAPIView, \
    WeatherQueryListCreateAPIView

urlpatterns = [
    path('', WeatherAPIView.as_view(), name='weather'),
    path('history/', WeatherQueryHistoryView.as_view(), name='weather_history'),
    path('api/queries/', WeatherQueryListCreateAPIView.as_view(), name='query-list'),
    path('api/queries/<int:pk>/', WeatherQueryRetrieveAPIView.as_view(), name='query-detail'),
]