# weather/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_weather_data
from django.shortcuts import render

class WeatherAPIView(APIView):
    def get(self, request, city):
        weather_data = get_weather_data(city)
        if weather_data:
            data = {
                "temperature": weather_data["current"]["temp_c"],
                "feels_like": weather_data["current"]["feelslike_c"],
                "humidity": weather_data["current"]["humidity"],
                "wind_speed": weather_data["current"]["wind_kph"],
                "wind_dir": weather_data["current"]["wind_dir"],
                "description": weather_data["current"]["condition"]["text"],
                "icon": weather_data["current"]["condition"]["icon"],
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Unable to fetch weather data."},
                status=status.HTTP_404_NOT_FOUND
            )

def index(request):
    return render(request, 'weather/index.html')