from django.shortcuts import render
from django.http import HttpResponse
import requests

API_KEY = 'VBPG6AVYZLFFBYEQVKJYWUUXM'
def index(request):
    return render(request, 'main/index.html')

def weather_check(request):
    city = request.GET.get('city')
    start = request.GET.get('start')
    end = request.GET.get('end')

    result = None
    days = None

    if city and start and end:
        weather = fetch_weather_data(city,API_KEY ,start, end)

        if weather:
            days = weather["days"]
            result = f"Нашёл {len(days)} дней прогноза"
        else:
            result = "Не удалось получить данные."

    return render(request, 'main/index.html', {
        'result': result,
        'days': days
    })


def fetch_weather_data(city, api_key, start, end):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start}/{end}"

    params = {
        "unitGroup": "metric",
        "include": "days",
        "key": api_key,
        "contentType": "json"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Ошибка запроса:", response.status_code, response.text)
        return None

    return response.json()

