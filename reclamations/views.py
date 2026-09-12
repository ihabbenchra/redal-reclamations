from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reclamation
from .forms import ReclamationForm, ReponseForm, StatutForm


def est_employe(user):
    return user.is_authenticated and user.est_employe()


def est_technicien(user):
    return user.is_authenticated and user.est_technicien()


@login_required
def accueil(request):
    if request.user.est_technicien():
        return redirect('liste_reclamations')
    return redirect('mes_reclamations')


@login_required
@user_passes_test(est_employe)
def deposer_reclamation(request):
    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            reclamation = form.save(commit=False)
            reclamation.employe = request.user
            reclamation.save()
            return redirect('mes_reclamations')
    else:
        form = ReclamationForm()
    return render(request, 'reclamations/deposer.html', {'form': form})


@login_required
@user_passes_test(est_employe)
def mes_reclamations(request):
    reclamations = Reclamation.objects.filter(employe=request.user)
    return render(request, 'reclamations/mes_reclamations.html', {'reclamations': reclamations})


@login_required
@user_passes_test(est_technicien)
def liste_reclamations(request):
    reclamations = Reclamation.objects.all()
    return render(request, 'reclamations/liste_reclamations.html', {'reclamations': reclamations})


@login_required
@user_passes_test(est_technicien)
def traiter_reclamation(request, pk):
    reclamation = get_object_or_404(Reclamation, pk=pk)
    reponse_existante = getattr(reclamation, 'reponse', None)

    if request.method == 'POST':
        statut_form = StatutForm(request.POST, instance=reclamation)
        reponse_form = ReponseForm(request.POST, instance=reponse_existante)
        if statut_form.is_valid() and reponse_form.is_valid():
            reclamation = statut_form.save(commit=False)
            reclamation.technicien = request.user
            reclamation.save()
            reponse = reponse_form.save(commit=False)
            reponse.reclamation = reclamation
            reponse.save()
            return redirect('liste_reclamations')
    else:
        statut_form = StatutForm(instance=reclamation)
        reponse_form = ReponseForm(instance=reponse_existante)

    return render(request, 'reclamations/traiter.html', {
        'reclamation': reclamation,
        'statut_form': statut_form,
        'reponse_form': reponse_form,
    })
