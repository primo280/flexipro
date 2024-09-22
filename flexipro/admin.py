from django.contrib import admin
from .models import *
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'soustitre')
    search_fields = ('id',)

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'profession', 'mot', 'image')
    search_fields = ('id',)