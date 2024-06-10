from time import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .models import *
from .forms import ChambreForm 
from .forms import PatientForm
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from datetime import datetime
# liaison
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def ajouter_chambre(request):
    user_id = request.session.get('user_id')
    chambres = Chambre.objects.all()
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        if form.is_valid():
            form.save()
            message_success = "L'ajout est effectué avec succès."
            user_id = request.session.get('user_id')
            chambres = Chambre.objects.all()
            return render(request, 'chambre.html', {'message_success': message_success, 'chambres': chambres, 'user_id': user_id}) 
        else:
            user_id = request.session.get('user_id')
            chambres = Chambre.objects.all()
            message_erreur = "Un problème est survenu lors de l'ajout de la chambre."
            return render(request, 'chambre.html', {'message_erreur': message_erreur, 'chambres': chambres, 'user_id': user_id})
    else:
        form = ChambreForm()
    return render(request, 'chambre.html', {'form': form, 'chambres': chambres, 'user_id': user_id})

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

@csrf_exempt
def chambre(request):
    if request.method == 'POST':
        temperature = request.POST.get('temperature')
        humidite = request.POST.get('humidite')
        qualite_air = request.POST.get('qualite_air')

        try:
            chambre = Chambre.objects.get(numero=1, etage=1)
            chambre.temperature = temperature
            chambre.humidite = humidite
            chambre.qualite_air = qualite_air
            chambre.save()
            return JsonResponse({'status': 'success'})
        except Chambre.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Chambre non trouvée'})

    else:
        chambres = Chambre.objects.all()
        return render(request, 'chambre.html', {'chambres': chambres})

def ajouter_patient(request):
    user_id = request.session.get('user_id')
    chambres = Chambre.objects.all()
    patients = Patient.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        chambre=request.POST.get('chambre')
        print(chambre)
        date_entree = datetime.strptime(request.POST.get('date_entree'), '%Y-%m-%d').date()
        date_sortie = datetime.strptime(request.POST.get('date_sortie'), '%Y-%m-%d').date()

        if form.is_valid():
            nb_patient_chambre = Patient.objects.filter(chambre=chambre).count()
            patients_dans_chambre = Patient.objects.filter(chambre=chambre)
            if nb_patient_chambre>=3 :
                for patient in patients_dans_chambre:
                    if date_entree < patient.date_sortie and date_sortie > patient.date_entree:
                        message_erreur = "Cette chambre n'est pas disponible pour les dates sélectionnées."
                        return render(request, 'patient.html', {'message_erreur': message_erreur, 'chambres': chambres, 'patients': patients, 'user_id': user_id})
                message_erreur = "Cette chambre est saturée."
                return render(request, 'patient.html', {'message_erreur': message_erreur, 'chambres':chambres , 'patients': patients, 'user_id': user_id})  

            form.save()
            message_success = "L'ajout est effectué avec succès."
            patients = Patient.objects.all()
            return render(request, 'patient.html', {'message_success': message_success, 'chambres':chambres , 'patients': patients, 'user_id': user_id}) 
        else:
            patients = Patient.objects.all()
            message_erreur = "Un problème est survenu lors de l'ajout de la patient."
            return render(request, 'patient.html', {'message_erreur': message_erreur, 'chambres':chambres , 'patients': patients, 'user_id': user_id})
    else:
        form = PatientForm()
    return render(request, 'patient.html', {'form': form, 'chambres':chambres , 'patients': patients, 'user_id': user_id})


def patients_json(request):
    patients = Patient.objects.all()
    data = [{'id': patient.id,'nom': patient.nom, 'prenom': patient.prenom, 'date_entree': patient.date_entree, 'date_sortie': patient.date_sortie} for patient in patients]
    return JsonResponse(data, safe=False)


def patient(request):
    user_id = request.session.get('user_id')
    patients = Patient.objects.all()
    chambres = Chambre.objects.all()
    return render(request, 'patient.html', {'patients': patients, 'chambres':chambres , 'user_id': user_id})

@csrf_exempt
def personnel(request):
    if request.method == 'POST':
        personnel_id = request.POST.get('personnel_id')
        
        try:
            personnel = Personnel.objects.get(pk=personnel_id)
            pointage = Pointage(personnel=personnel)
            pointage.save()
            return JsonResponse({'status': 'success'})
        except Personnel.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Personnel non trouvé'})
    else:
        personnels = Personnel.objects.all()
        return render(request, 'personnel.html', {'personnels': personnels})    

def ajouter_personnel(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        est_medecin = 'est_medecin' in request.POST
        ci = request.POST.get('ci')
        personnel = Personnel(ci=ci, nom=nom, prenom=prenom, est_medecin=est_medecin)
        personnel.save()
        return redirect('personnel')
    else:
        personnels = Personnel.objects.all()
        return render(request, 'personnel.html', {'personnels': personnels})

#  liaison
@csrf_exempt
def rfid_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Extract RFID and sensor data
            rfid = data.get('rfid')
            temperature = data.get('temperature')
            humidity = data.get('humidity')
            gas = data.get('gas')
            # Process and save the data as needed
            # Example: RFIDData.objects.create(rfid=rfid, temperature=temperature, humidity=humidity, gas=gas)
            return JsonResponse({'status': 'success', 'message': 'Data received'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
