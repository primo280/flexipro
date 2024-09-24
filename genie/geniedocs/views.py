from django.shortcuts import render
from .models import *
def base(request):
    return render (request, 'geniedocs/base.html')

def home(request):
    categories = Categorie.objects.all()  # Récupérer toutes les catégories
    cours = Cours.objects.all()  # Récupérer tous les cours
    return render (request, 'geniedocs/home.html', {
        'categories': categories,
        'cours': cours,
    })

