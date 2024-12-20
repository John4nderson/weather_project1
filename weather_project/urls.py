from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),  # Маршрут для weather приложения

    # Новый маршрут для пустого пути
    path('', lambda request: redirect('weather/')),  # Перенаправление на /weather/
]
