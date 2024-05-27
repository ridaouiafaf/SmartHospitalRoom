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
