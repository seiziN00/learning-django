from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('greetings/', views.greetings, name='greetings'),
    path('today/', views.today, name='today')
]
