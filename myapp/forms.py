from django import forms

from django import forms
from .models import *

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['numero', 'etage']
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['id', 'nom', 'prenom', 'date_entree', 'date_sortie','chambre']
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['nom', 'prenom', 'est_medecin', 'date_pointage']  

        

