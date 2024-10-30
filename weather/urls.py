# weather/urls.py
from django.urls import path
from .views import WeatherAPIView, index

urlpatterns = [
    path('', index, name='index'),
    path('api/weather/<str:city>/', WeatherAPIView.as_view(), name='weather_api'),
]
