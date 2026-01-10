from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    city = request.GET.get('city')
    result = None

    if city:
        result = f"Идёт проверка условий для города {city}..."

    data = {
        'result': result
    }

    return render(request, 'main/index.html', data)
