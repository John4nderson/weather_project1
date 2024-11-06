from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import City, Weather
import requests
from decouple import config  # Для загрузки переменных из .env

# Загрузка API-ключа из .env
API_KEY = config('WEATHER_API_KEY')

def get_weather_data(city_name):
    """Функция для получения данных о погоде из OpenWeatherMap API."""
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather",
        params={"q": city_name, "appid": API_KEY, "units": "metric", "lang": "ru"}
    )
    response.raise_for_status()
    return response.json()

def save_weather_data(city_name):
    """Функция для сохранения данных о погоде в базе данных."""
    weather_data = get_weather_data(city_name)

    # Сохранение или создание записи города
    city, _ = City.objects.get_or_create(name=weather_data["name"])

    # Сохранение данных о погоде
    Weather.objects.create(
        city=city,
        temperature=weather_data["main"]["temp"],
        description=weather_data["weather"][0]["description"],
        wind_speed=weather_data["wind"]["speed"],
        humidity=weather_data["main"]["humidity"],
        pressure=weather_data["main"]["pressure"]
    )

def weather_view(request, city_name):
    """Представление для получения данных о погоде и сохранения их в базу."""
    try:
        save_weather_data(city_name)  # Сохраняем данные о погоде
        city = get_object_or_404(City, name=city_name)
        weather_reports = city.weather_reports.all().order_by('-recorded_at')
        return render(request, 'weather_table.html', {
            "city": city,
            "weather_reports": weather_reports
        })
    except requests.exceptions.RequestException:
        return JsonResponse({"error": "Ошибка при запросе данных о погоде"}, status=500)
