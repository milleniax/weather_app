from django.shortcuts import render
from . models import City
from .forms import CityForm

import requests

def index(request):
    key = 'd559b5a4376f23ea431a0c10cf745ab7'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + key

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request , 'index.html',context)
