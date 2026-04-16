from django.shortcuts import render
from django.http import HttpResponse


def test(request):
  return HttpResponse("It works!")

def create(request):
  return HttpResponse("Create a comment")