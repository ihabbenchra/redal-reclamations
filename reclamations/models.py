from django.conf import settings
from django.db import models


class Reclamation(models.Model):
    EN_ATTENTE = 'EN_ATTENTE'
    EN_COURS = 'EN_COURS'
    RESOLUE = 'RESOLUE'
    STATUT_CHOICES = [
        (EN_ATTENTE, 'En attente'),
        (EN_COURS, 'En cours'),
        (RESOLUE, 'Résolue'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    anonyme = models.BooleanField(default=False)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default=EN_ATTENTE)
    employe = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reclamations')
    technicien = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='reclamations_traitees')

    def consulterEtat(self):
        return self.statut

    def nom_auteur(self):
        if self.anonyme:
            return 'Anonyme'
        return self.employe.username

    class Meta:
        ordering = ['-dateCreation']

    def __str__(self):
        return self.titre


class Reponse(models.Model):
    reclamation = models.OneToOneField(Reclamation, on_delete=models.CASCADE, related_name='reponse')
    contenu = models.TextField()
    dateReponse = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réponse à {self.reclamation.titre}"
