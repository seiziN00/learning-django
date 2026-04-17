from django.shortcuts import render
from django.http import HttpResponse
from .models import Author


def queries(request):
  authors = Author.objects.all()

  filtered = Author.objects.filter(email='janegonzalez@example.org')

  author = Author.objects.get(id=1)

  offsets = Author.objects.all()[5:10]

  return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'offsets': offsets})