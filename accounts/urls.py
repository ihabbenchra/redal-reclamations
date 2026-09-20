from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('inscription/employe/', views.inscription_employe, name='inscription_employe'),
    path('inscription/technicien/', views.inscription_technicien, name='inscription_technicien'),
    path('connexion/', views.ConnexionView.as_view(), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='connexion'), name='deconnexion'),
]