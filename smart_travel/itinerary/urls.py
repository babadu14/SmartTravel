from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = DefaultRouter()
router.register('itinerary', views.ItineraryViewSet)

itinerary_routers = routers.NestedDefaultRouter(
    router,
    'itinerary',
    lookup = 'itinerary'
)

itinerary_routers.register('activity', views.ActivityViewSet, basename='itinerary-activity')


urlpatterns = [
    path('weather/', views.weather_view, name='weather'),
    path('', include(router.urls)),
    path('', include(itinerary_routers.urls)),

]