from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date


def create(request):
  reporter = Reporter(first_name='Alexander', last_name='Magno', email='alexmangum@example.com')
  reporter.save()

  article1 = Article(headline='Django is cool', pub_date=date(2005, 7, 27), reporter=reporter)
  article1.save()

  article2 = Article(headline='React is great', pub_date=date(2005, 8, 16), reporter=reporter)
  article2.save()

  article3 = Article(headline='Python is awesome', pub_date=date(2005, 11, 4), reporter=reporter)
  article3.save()

  # result = article1.reporter.first_name
  # result = reporter.article_set.all()
  # result = reporter.article_set.filter(headline__startswith='Django')
  result = reporter.article_set.count()

  return HttpResponse(result)