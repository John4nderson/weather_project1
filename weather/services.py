# weather/services.py
# weather/services.py

import requests
from django.conf import settings

def get_weather_data(city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": settings.WEATHER_API_KEY,
        "q": city,
        "aqi": "no",
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Это вызовет исключение при ошибке
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

