from django import forms
from .models import Chambre

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'etage', 'temperature', 'humidite', 'qualite_air']

from django import forms
from .models import *

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'etage']
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['id', 'nom', 'prenom', 'date_entree', 'date_sortie', 'chambre']
