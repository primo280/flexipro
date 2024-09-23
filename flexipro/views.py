from django.shortcuts import render
from .models import *
# Create your views here.
def base (request):
    heros = Hero.objects.all()
    return render(request, 'base.html', {'heros': heros})


def home (request):
    heros = Hero.objects.all()
   
    
    return render(request, 'flexipro/home.html', {'heros': heros})

