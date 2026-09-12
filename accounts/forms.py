from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Utilisateur.ROLE_CHOICES)

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'role', 'password1', 'password2']

    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        utilisateur.email = self.cleaned_data['email']
        utilisateur.role = self.cleaned_data['role']
        if commit:
            utilisateur.save()
        return utilisateur
