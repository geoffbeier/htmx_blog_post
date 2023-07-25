from django.conf import settings
from django.db import models


class Trip(models.Model):
    class Country(models.TextChoices):
        FRANCE = "FR", "France"
        SPAIN = "ES", "Spain"
        GERMANY = "DE", "Germany"

    country = models.CharField(max_length=3, choices=Country.choices)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.country}] {self.origin} -> {self.destination}"


class Vacation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    trip = models.ForeignKey(
        "trip_builder.Trip", related_name="vacations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"[{self.user}] {self.name}: Trip from {self.trip.origin} to {self.trip.destination}"
