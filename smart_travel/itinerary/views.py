from django.shortcuts import render
from django.http import JsonResponse
import requests
from dotenv import load_dotenv
import os
from rest_framework.permissions import IsAuthenticated
from itinerary.serializers import ActivitySerilizer, ItinerarySerializer
from itinerary.models import Itinerary, Activity
from rest_framework import viewsets

load_dotenv()

def get_weather(location):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    return response.json()

def weather_view(request):
    city = request.GET.get('location')
    weather_data = None
    
    if city:
        weather_data = get_weather(city)
    
    return render(request, 'weather.html', {'weather': weather_data,'city': city})


class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)
    
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerilizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        itinerary_id = self.kwargs['itinerary_id']
        return Activity.objects.get(id=itinerary_id)
    
    def perform_create(self, serializer):
        itinerary_id = self.kwargs['itinerary_id']
        itinerary = Itinerary.objects.get(id=itinerary_id)
        return serializer.save(itinerary=itinerary)