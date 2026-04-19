from django.http import HttpResponse
from django.shortcuts import render


def form(request):
  return render(request, 'index.html', {})


def goal(request):
  if request.method == 'GET':
    name = request.GET['name']
    message = request.GET['message']
    return render(request, 'success.html', {'name': name, 'message': message})
  else:
    return HttpResponse("POST no está soportado")