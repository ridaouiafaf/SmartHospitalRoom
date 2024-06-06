from django.db import models

class Chambre(models.Model):
    id = models.AutoField(primary_key=True)  # Champ AutoField pour l'identifiant unique
    numero = models.IntegerField()
    etage = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidite = models.DecimalField(max_digits=5, decimal_places=2)
    qualite_air = models.CharField(max_length=100)

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
    date_sortie = models.DateField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom', 'prenom'], name='unique')
        ]

    def __str__(self):
        return f"Patient {self.nom} {self.prenom}"
    
class Personnel(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    est_medecin = models.BooleanField(default=False)
    fonctionnalite = models.CharField(max_length=100)  # Ajout du champ fonctionnalité
    date_pointage = models.DateTimeField(null=True, blank=True)  # Nouveau champ

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
