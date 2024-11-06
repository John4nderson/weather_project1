
# Weather Service 🌤️

## Описание

Простой сервис для просмотра текущей погоды в выбранных городах. Доступна информация о температуре, влажности, ветре и погодных условиях.

## Стек технологий

- **Backend**: Django, Django Rest Framework
- **Frontend**: Bootstrap
- **API**: [WeatherAPI](https://www.weatherapi.com/)

## Установка

1. **Клонировать репозиторий**:
   ```bash
   git clone https://github.com/John4nderson/weather_project1.git
   cd weather_project
   ```

2. **Установить зависимости**:
   ```bash
   pip install poetry
   poetry install
   ```

3. **Настроить API-ключ**:
   - Создайте файл `.env` в корне проекта.
   - Добавьте свой ключ:
     ```plaintext
     WEATHER_API_KEY=your_api_key_here
     ```

4. **Запустить миграции и сервер**:
   ```bash
   poetry run python manage.py migrate
   poetry run python manage.py runserver
   ```

5. **Открыть приложение**:
   Перейдите в браузере по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Быстрый старт

- Введите название города на главной странице или выберите из популярных городов для просмотра погоды.
