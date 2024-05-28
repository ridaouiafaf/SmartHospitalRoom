from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .models import *
from .forms import ChambreForm 
from .forms import PatientForm
from django.http import JsonResponse
from django.contrib.sessions.models import Session

def ajouter_chambre(request):
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        if form.is_valid():
            form.save()
            message_success = "L'ajout est effectué avec succès."
            return render(request, 'chambre.html', {'message_success': message_success}) 
        else:
            message_erreur = "Un problème est survenu lors de l'ajout de la chambre."
            return render(request, 'chambre.html', {'message_erreur': message_erreur})
    else:
        form = ChambreForm()
    return render(request, 'chambre.html', {'form': form})

def chambres_json(request):
    chambres = Chambre.objects.all()
    data = [{'numero': chambre.numero, 'etage': chambre.etage, 'temperature': chambre.temperature, 'humidite': chambre.humidite, 'qualite_air': chambre.qualite_air} for chambre in chambres]
    return JsonResponse(data, safe=False)

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Nom d'utilisateur ou mot de passe incorrect.")
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = '/'


def index(request):    
    user_id = request.user.id
    request.session['user_id'] = user_id
    return render(request, 'index.html')

def chambre(request):
    user_id = request.session.get('user_id')
    chambres = Chambre.objects.all()
    return render(request, 'chambre.html', {'chambres': chambres, 'user_id': user_id})



def ajouter_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            message_success = "L'ajout est effectué avec succès."
            return render(request, 'patient.html', {'message_success': message_success}) 
        else:
            message_erreur = "Un problème est survenu lors de l'ajout de la patient."
            return render(request, 'patient.html', {'message_erreur': message_erreur})
    else:
        form = PatientForm()
    return render(request, 'patient.html', {'form': form})

def patients_json(request):
    patients = Patient.objects.all()
    data = [{'id': patient.id,'nom': patient.nom, 'prenom': patient.prenom, 'date_entree': patient.date_entree, 'date_sortie': patient.date_sortie} for patient in patients]
    return JsonResponse(data, safe=False)


def patient(request):
    user_id = request.session.get('user_id')
    patients = Patient.objects.all()
    return render(request, 'patient.html', {'patients': patients, 'user_id': user_id})