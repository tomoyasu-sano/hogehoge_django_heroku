from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import SayHoge


class SayHogeListView(ListView):
    model = SayHoge
    #context_object_name = "blogs"