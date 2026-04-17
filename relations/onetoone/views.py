from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant


def create(request):
  place = Place(name='Django', address='Internet')
  place.save()

  restaurant = Restaurant(place=place, number_of_employees=7)
  restaurant.save()

  return HttpResponse(restaurant.place.name)