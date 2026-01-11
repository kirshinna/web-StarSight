from django.shortcuts import render
from django.http import HttpResponse
from .utils import prepare_heatmap_matrix, generate_hourly_heatmap
import requests

API_KEY = 'GXNLFKRGXCQY4U79VPMBGRXZM'
def index(request):
    return render(request, 'main/home.html')

def weather_check(request):

    heatmap_img = None
    result = None
    days = None

    if request.method == "POST":
        city = request.POST.get("city")
        start = request.POST.get("start")
        end = request.POST.get("end")

        if city and start and end:
            weather = fetch_weather_data(city, API_KEY, start, end)

            if weather:
                days = weather["days"]
                df = prepare_heatmap_matrix(days)
                heatmap_img = generate_hourly_heatmap(df)
                result = f"Ночная карта {len(days)} дней."
            else:
                result = "Не удалось получить данные."

        return render(request, "main/heatmap.html", {
            "result": result,
            "heatmap_img": heatmap_img,
            "days": days
        })

    return render(request, "main/heatmap.html")

def fetch_weather_data(city, api_key, start, end):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start}/{end}"

    params = {
        "unitGroup": "metric",
        "include": "hours",
        "key": api_key,
        "contentType": "json"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Ошибка запроса:", response.status_code, response.text)
        return None

    return response.json()


