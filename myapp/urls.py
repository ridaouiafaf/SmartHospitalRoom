from django.urls import path
from .views import *

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('index/', index, name='index'),
    path('chambre/', chambre, name='chambre'),
    path('ajouter_chambre/', ajouter_chambre, name='ajouter_chambre'),
    path('chambres/json/', chambres_json, name='chambres_json'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
