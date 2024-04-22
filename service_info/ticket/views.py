from django.shortcuts import render, redirect

from .models import Ticket
from .forms import *


def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket/index.html', {'tickets': tickets})

## CRUD pour les tickets
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TicketForm()
    return render(request, 'ticket/create_ticket.html', {'form': form})

def read_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket/affiche_ticket.html', {'ticket': ticket})

def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.delete()
    return redirect('index')

def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = TicketForm(instance=ticket)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'ticket/update_ticket.html', {'form': form, 'ticket': ticket})

def traitement_ticket(request):
    lform = TicketForm(request.POST)
    if lform.is_valid():
        ticket = lform.save()
        return render(request, 'ticket/affiche_ticket.html', {'Ticket': ticket})
    else:
        return render(request, 'ticket/create_ticket.html', {'form': lform})
    
    
def search_ticket(request):
    if request.method == 'POST':
        lform = TicketIdForm(request.POST)
        if lform.is_valid():
            ticket_id = lform.cleaned_data['ticket_id']
            return redirect('ticket:read_ticket', ticket_id=ticket_id)
    else:
        lform = TicketIdForm()
    return render(request, 'ticket/search_ticket.html', {'form': lform})
    
    
    
    
    
def create_category(request):
    """Création d'une catégorie."""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'ticket/create_category.html', {'form': form})

def traitement_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return render(request, 'ticket/affiche_category.html', {'category': category})
    else:
        form = CategoryForm()
    return render(request, 'ticket/create_category.html', {'form': form})

def read_category(request, category_id):
    """Recherche par id de la catégorie et affiche les détails de la catégorie."""
    category = Category.objects.get(id=category_id)
    return render(request, 'ticket/affiche_category.html', {'category': category})

def delete_category(request, category_id):
    """Suppression d'une catégorie par id."""
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('index')

def update_category(request, category_id):
    """Update d'une catégorie par id."""
    category = Category.objects.get(id=category_id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'ticket/update_category.html', {'form': form, 'category': category})
