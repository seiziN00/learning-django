from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def greetings(request):
    return render(request, 'greetings.html', {})

def today(request):
    return render(request, 'today.html', {})