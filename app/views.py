from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

from django.contrib import admin
from django.urls import path
from .views import index
urlpatterns = [
path("", index),]


