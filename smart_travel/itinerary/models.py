from django.db import models

class Itinerary(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    destiantion = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')
    route = models.TextField()
    activities = models.TextField()


class Activity(models.Model):
    itinerary = models.ForeignKey(Itinerary, related_name='activities', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)   