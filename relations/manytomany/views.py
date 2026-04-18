from django.shortcuts import render
from .models import Publication, Article
from django.http import HttpResponse


def create(request):
  Article.objects.all().delete()
  Publication.objects.all().delete()

  art1 = Article(headline="Artículo primero")
  art1.save()
  art2 = Article(headline="Artículo segundo")
  art2.save()
  art3 = Article(headline="Artículo tercero")
  art3.save()

  pub1 = Publication(title="Publicación primera")
  pub1.save()
  pub2 = Publication(title="Publicación segunda")
  pub2.save()
  pub3 = Publication(title="Publicación tercera")
  pub3.save()
  pub4 = Publication(title="Publicación cuarta")
  pub4.save()
  pub5 = Publication(title="Publicación quinta")
  pub5.save()
  pub6 = Publication(title="Publicación sexta")
  pub6.save()
  pub7 = Publication(title="Publicación séptima")
  pub7.save()

  art1.publications.add(pub1)
  art1.publications.add(pub2)
  art1.publications.add(pub3)
  art2.publications.add(pub4)
  art2.publications.add(pub5)
  art3.publications.add(pub6)
  art3.publications.add(pub7)

  # art1.publications.remove(pub2)
  # art1.publications.get(id=3)

  result = art1.publications.all()

  return HttpResponse(result)