from django import forms
from .models import Chambre

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'etage', 'temperature', 'humidite', 'qualite_air']

