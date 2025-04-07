from django.shortcuts import render
from django.http import JsonResponse
import requests

def get_weather(location):
    api_key = "5146a9c6175342399cf194859250704"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    return response.json()

def weather_view(request):
    city = request.GET.get('location')
    weather_data = None
    
    if city:
        weather_data = get_weather(city)
    
    return render(request, 'weather.html', {'weather': weather_data,'city': city})

