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
<<<<<<< HEAD
        fields = ['id', 'nom', 'prenom', 'date_entree', 'date_sortie']
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['nom', 'prenom', 'est_medecin', 'date_pointage']  
=======
        fields = ['id', 'nom', 'prenom', 'date_entree', 'date_sortie', 'chambre']
>>>>>>> 0449b61d3903fb57e05f749e9749e1ac173aa736
