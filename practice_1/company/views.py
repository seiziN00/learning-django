from django.http import HttpResponse
from .models import *


def create(request):
  return HttpResponse("Creating...")