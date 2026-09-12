from django import forms
from .models import Reclamation, Reponse


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['titre', 'description', 'anonyme']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'anonyme': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ReponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class StatutForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['statut']
        widgets = {
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }
