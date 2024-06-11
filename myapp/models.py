from django.db import models
from datetime import date
from django.utils import timezone

class Chambre(models.Model):
    id = models.AutoField(primary_key=True)  
    numero = models.IntegerField()
    etage = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    humidite = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    qualite_air = models.CharField(max_length=100, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['numero', 'etage'], name='unique_chambre')
        ]

    def __str__(self):
        return f"Chambre {self.numero} - Etage {self.etage}"


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_entree = models.DateField()
    date_sortie = models.DateField(default=date(2024, 1, 1))
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)

    def __str__(self):
        return f"Patient {self.nom} {self.prenom}"
    
class Personnel(models.Model):
    ci = models.CharField(max_length=100, primary_key=True) 
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    est_medecin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Pointage(models.Model):
    id = models.AutoField(primary_key=True)
    date_pointage = models.DateTimeField(default=timezone.now)
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Pointage {self.date_pointage} - {self.personnel}"
