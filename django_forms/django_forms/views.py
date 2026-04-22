from django.shortcuts import render
from .forms import CommentForm
from django.http import HttpResponse


def form(request):
  comment_form = CommentForm({'name': 'Dante', 'web_page': 'https://www.google.com', 'comment': 'Hola desde Django'})
  return render(request, 'form.html', {'comment_form': comment_form})


def goal(request):
  if request.method != 'POST':
    return HttpResponse('Método no válido')

  name = request.POST.get("name")
  web_page = request.POST.get("web_page")
  comment = request.POST.get("comment")
 
  return render(request, 'goal.html', {'name': name, 'web_page': web_page, 'comment': comment})