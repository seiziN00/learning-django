from django.shortcuts import render
import random


def home(request):
  return render(request, 'home.html', {})

def blog(request):
  numbers = [random.randint(1, 200) for i in range(10)]
  return render(request, 'blog.html', {'numbers': numbers})