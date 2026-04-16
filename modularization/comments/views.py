from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
from datetime import datetime


def test(request):
    return HttpResponse("It works!")


def create(request):
    #comment = Comment(name="Luis", score=3, comment="It's ok", date=datetime.now().date())
    #comment.save()
    return HttpResponse(f"It's for create comments")


def delete(request):
    comment = Comment.objects.get(id=2)
    comment.delete()
    return HttpResponse(f"It's for delete comments")