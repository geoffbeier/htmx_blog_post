from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render

from django import forms

from .models import Vacation, Trip


@login_required
def index(request):
    vacations = Vacation.objects.filter(user=request.user)
    return render(request, "index.html", context={"trips": vacations})


@login_required
def new_vacation(request):
    form = VacationForm()
    vacations = Vacation.objects.all()
    if request.method == "POST":
        form = VacationForm(request.POST)
        if form.is_valid():
            trip = Vacation.objects.create(
                user=request.user,
                name=form.cleaned_data["name"],
                trip_id=form.cleaned_data["itinerary"],
            )
            print(f"Created trip: {trip}")
            return render(request, "index_reset.html", context={"trips": vacations})
        else:
            print(f"Form is invalid: {form.errors}")
    elif "reset" in request.GET:
        return render(request, "index_reset.html", context={"trips": vacations})
    return render(request, "new_vacation.html", context={"form": form})


@login_required
def country_itineraries(request):
    if request.method != "POST":
        return HttpResponseBadRequest()
    form = VacationForm(request.POST)
    return render(request, "itinerary_choice.html", context={"form": form})


class VacationForm(forms.Form):
    name = forms.CharField(required=True)
    country = forms.ChoiceField(required=True)
    itinerary = forms.ChoiceField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["country"].choices = [("", "Please select a country")] + [
            c
            for c in Trip.Country.choices
            if Trip.objects.filter(country=c[0]).count() > 0
        ]

        self.set_itineraries()

    def set_itineraries(self):
        country = self.data.get("country", "")
        itinerary_options = [("", "Please select an itinerary")]
        available_itineraries = Trip.objects.filter(country=country)
        if available_itineraries:
            itinerary_options += [
                (i.id, " - ".join([i.origin, i.destination]))
                for i in available_itineraries
            ]
        self.fields["itinerary"].choices = itinerary_options
