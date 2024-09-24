from django.contrib import admin
from .models import *

# Inline pour permettre l'ajout de documents directement dans l'admin de Cours
class DocumentInline(admin.TabularInline):
    model = Cours.documents.through  # Utilisation du ManyToManyField
    extra = 1  # Nombre de formulaires vierges pour les nouveaux documents

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom']  # Affichage des champs dans la liste de l'admin
    search_fields = ['nom']  # Ajout d'une barre de recherche


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'prix', 'image']  # Affichage des cours et des catégories dans la liste de l'admin
    search_fields = ['titre', 'categorie__nom']  # Barre de recherche pour les titres de cours et catégories
    list_filter = ['categorie']  # Filtrage par catégorie dans l'admin
    inlines = [DocumentInline]  # Ajouter des documents directement dans l'admin de Cours

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['description', 'fichier']  # Affichage des champs dans la liste de l'admin
    search_fields = ['description']  # Barre de recherche pour les descriptions de documents
