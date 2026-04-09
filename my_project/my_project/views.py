from django.http import HttpResponse
from django.shortcuts import render


def greetings(request):
    return HttpResponse("Hello, Django!")

def goodbye(request):
    return HttpResponse("Bye bye Django!")

# With CSS styles
def howareyou(request):
    return HttpResponse("<p style='color: #0f0; background-color: #333; padding: 1rem; border-radius: 12px;'>How are you?</p>")

def person(request, age):
    if age >= 18:
        return HttpResponse("You are an adult!")
    else:
        return HttpResponse("You aren't an adult")

def simple(request):
    return render(request, "simple.html", {})

def dynamic(request, name):
    stack = ["Python", "JavaScript", "Django", "Node", "React"]
    context = {"name": name, "stack": stack}
    return render(request, "dynamic.html", context)

def home(request):
    return render(request, "index.html", {})