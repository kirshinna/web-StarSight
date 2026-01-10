from django.shortcuts import render
from django.http import HttpResponse
import requests

API_KEY = '12c340b2c8e9d94fdb3c80b1c9daebd4'

def index(request):
    city = request.GET.get('city')
    result = None

    if city:
        result = fetch_weather_data(city, API_KEY)

    else:
        result = "Не удалось получить данные о погоде."

    data = {
        'result': result
    }

    return render(request, 'main/index.html', data)


def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        print("Ошибка запроса:", response.status_code, response.text)
        return None

    data = response.json()

    return data
