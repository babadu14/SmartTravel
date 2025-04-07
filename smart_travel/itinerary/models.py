from django.db import models

class Itinerary(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    destiantion = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')
    route = models.TextField()
    activities = models.TextField()


class Activity(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    