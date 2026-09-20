from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


class InscriptionEmployeForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        utilisateur.email = self.cleaned_data['email']
        utilisateur.role = Utilisateur.EMPLOYE
        if commit:
            utilisateur.save()
        return utilisateur


class InscriptionTechnicienForm(UserCreationForm):
    email = forms.EmailField(required=True)
    code_invitation = forms.CharField(label="Code d'invitation technicien")

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2']

    def clean_code_invitation(self):
        code = self.cleaned_data['code_invitation']
        if code != 'REDAL-TECH-2025':
            raise forms.ValidationError("Code d'invitation invalide.")
        return code

    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        utilisateur.email = self.cleaned_data['email']
        utilisateur.role = Utilisateur.TECHNICIEN
        if commit:
            utilisateur.save()
        return utilisateur