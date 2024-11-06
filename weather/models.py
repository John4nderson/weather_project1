from django.db import models

class City(models.Model):
    """
    Модель для хранения данных о городе.
    """
    name = models.CharField(max_length=100, unique=True)  # Уникальное название города

    def __str__(self):
        return self.name


class Weather(models.Model):
    """
    Модель для хранения данных о погоде.
    """
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="weather_reports"
    )  # Связь с городом
    temperature = models.FloatField()  # Температура в градусах Цельсия
    description = models.CharField(max_length=200)  # Краткое описание погоды
    wind_speed = models.FloatField()  # Скорость ветра в м/с
    humidity = models.IntegerField()  # Влажность в процентах
    pressure = models.IntegerField()  # Давление в гПа
    recorded_at = models.DateTimeField(auto_now_add=True)  # Время записи данных

    def __str__(self):
        return f"{self.city.name}: {self.temperature}°C, {self.description} ({self.recorded_at})"
