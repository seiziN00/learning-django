from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry


def update(request):
  author = Author.objects.get(id=1)
  author.name = "Sirio"
  author.email = 'sirius2000@demo.com'
  author.save()
  return HttpResponse("Modificado 👍")


def queries(request):
  authors = Author.objects.all()

  filtered = Author.objects.filter(email='janegonzalez@example.org')

  author = Author.objects.get(id=1)

  offsets = Author.objects.all()[5:10]

  word = Author.objects.filter(name__contains='phone')

  return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'offsets': offsets, 'word': word})