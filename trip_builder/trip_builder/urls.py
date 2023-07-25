from django.urls import path

from . import views

app_name = "trip_builder"

urlpatterns = [
    path("", views.index, name="index"),
    path("new_vacation", views.new_vacation, name="new_vacation"),
    path("country_itineraries", views.country_itineraries, name="country_itineraries"),
]
