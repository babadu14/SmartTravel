from itinerary.models import Itinerary, Activity
from rest_framework import serializers

class ActivitySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        exclude = ['itinerary', 'users']

class ItinerarySerializer(serializers.ModelSerializer):
    activity = ActivitySerilizer(many=True, read_only = True)

    class Meta:
        model = Itinerary
        exclude = ['user']
