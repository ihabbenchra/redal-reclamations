from django.contrib.auth.models import AbstractUser
from django.db import models


class Utilisateur(AbstractUser):
    EMPLOYE = 'EMPLOYE'
    TECHNICIEN = 'TECHNICIEN'
    ROLE_CHOICES = [
        (EMPLOYE, 'Employé'),
        (TECHNICIEN, 'Technicien'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYE)

    def est_employe(self):
        return self.role == self.EMPLOYE

    def est_technicien(self):
        return self.role == self.TECHNICIEN

    def __str__(self):
        return self.username
