from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    #path("", include('my_app.urls'), name='home'),
    path("", views.home, name="home"),
    path("greetings/", views.greetings, name="greetings"),
    path("goodbye/", views.goodbye, name="goodbye"),
    path("howareyou/", views.howareyou, name="howareyou"),
    path("person/<int:age>/", views.person, name="person"),
    path("simple/", views.simple, name="simple"),
    path("dynamic/<str:name>", views.dynamic, name="dynamic"),
    path('admin/', admin.site.urls),
]
