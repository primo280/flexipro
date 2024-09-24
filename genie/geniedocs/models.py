from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Document(models.Model):
    fichier = models.FileField(upload_to='documents/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description[:50]


class Cours(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.IntegerField(max_length=4 ,null=True,blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='cours')
    description = models.TextField()
    documents = models.ManyToManyField(Document, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Nouveau champ d'image


    def __str__(self):
        return self.titre

