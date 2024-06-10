from django.urls import path
from .views import *
# from .views import rfid_data

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('index/', index, name='index'),
    path('chambre/', chambre, name='chambre'),
    path('ajouter_chambre/', ajouter_chambre, name='ajouter_chambre'),
    path('chambres/json/', chambres_json, name='chambres_json'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('patient/', patient, name='patient'),
    path('ajouter/', ajouter_patient, name='ajouter_patient'),
    path('personnel/', personnel, name='personnel'),
    path('ajouter_personnel/', ajouter_personnel, name='add_personnel'),
    path('api/rfid_data/', rfid_data, name='rfid_data'), #pour la liaison
    
]
