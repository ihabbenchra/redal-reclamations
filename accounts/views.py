from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import InscriptionEmployeForm, InscriptionTechnicienForm


def inscription_employe(request):
    if request.method == 'POST':
        form = InscriptionEmployeForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)
            return redirect('accueil')
    else:
        form = InscriptionEmployeForm()
    return render(request, 'accounts/inscription.html', {'form': form})


def inscription_technicien(request):
    if request.method == 'POST':
        form = InscriptionTechnicienForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)
            return redirect('accueil')
    else:
        form = InscriptionTechnicienForm()
    return render(request, 'accounts/inscription.html', {'form': form})


class ConnexionView(LoginView):
    template_name = 'accounts/connexion.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.is_superuser:
            messages.error(
                self.request,
                "Les comptes administrateur doivent se connecter via /admin/."
            )
            return self.form_invalid(form)
        return super().form_valid(form)