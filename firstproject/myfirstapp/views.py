from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')

def data(request):
    """Affiche un formulaire de saisie de nom."""
    return render(request, 'myfirstapp/formulaire.html')

def bonjour(request):
    """Récupère le nom saisi dans le formulaire et l'affiche dans une page de salutation."""
    nom=request.GET['nom']
    return render(request, 'myfirstapp/bonjour.html', {'nom': nom})
