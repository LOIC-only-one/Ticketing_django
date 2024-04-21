from django.shortcuts import render
from .forms import LivreForm
from .models import Livre
from django.http import HttpResponseRedirect
from .models import models
# Create your views here.

def index(request):
    return render(request, 'bibliotheque/index.html')


def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            Livre = form.save()
            return render(request, 'bibiliotheque/affiche.html', {'Livre': Livre})
        else:
            return render(request, 'bibliotheque/ajout.html', {'form': form})
    else:
        form = LivreForm()
        return render(request, 'bibliotheque/ajout.html', {'form': form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request, 'bibliotheque/affiche.html', {'Livre': Livre})
    else:
        return render(request, 'bibliotheque/ajout.html', {'form': lform})


def all(request):
    Livres = Livre.objects.all()
    return render(request, 'bibliotheque/read.html', {'Livres': Livres})


def read(request,id):
    Livres = Livre.objects.get(id=id)
    return render(request, 'bibliotheque/affiche.html', {'Livre': Livres})


### Pas encore finis le update
def update(request,id):
    form = LivreForm(request.POST)
    if form.is_valid():
        Livre = form.save()

        Livre.id = id
        Livre.save()
        return HttpResponseRedirect('/bibliotheque/all/') ## redirige vers la page all en cas de succès
    else:
        return render(request, 'bibliotheque/update.html', {'form': form, "id": id})



def delete(request,id):
    Livres = Livre.objects.get(id=id)
    Livres.delete()
    return render(request, 'bibliotheque/delete.html', {'Livre': Livres})