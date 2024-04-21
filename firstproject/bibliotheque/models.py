from django.db import models

# Create your models here.

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    nombre_page = models.IntegerField(blank=False)
    date_parution = models.DateField()
    resume = models.TextField(null= True, blank=True)



    def __str__(self):
        chaine = f"{self.titre} de {self.auteur} edité le {self.date_parution}, le livre contient {self.nombre_page} pages.\n l'id du livre est {self.id}"
        return chaine

