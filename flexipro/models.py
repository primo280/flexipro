from django.db import models

class Hero(models.Model):
    titre = models.TextField(max_length=255, blank=True, null=True)    
    soustitre = models.TextField(blank=True, null=True)    

class Temoignage(models.Model):
    nom = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)     
    mot = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Image de profil") 
      