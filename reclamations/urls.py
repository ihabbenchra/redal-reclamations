from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('deposer/', views.deposer_reclamation, name='deposer_reclamation'),
    path('mes-reclamations/', views.mes_reclamations, name='mes_reclamations'),
    path('liste/', views.liste_reclamations, name='liste_reclamations'),
    path('<int:pk>/traiter/', views.traiter_reclamation, name='traiter_reclamation'),
]
