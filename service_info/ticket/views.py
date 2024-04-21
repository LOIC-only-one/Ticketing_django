from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket

def index(request):
    tickets = Ticket.objects.all()  # Récupère tous les tickets
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
    return render(request, 'ticket/read_ticket.html', {'ticket': ticket})

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
            return redirect('index')  # Redirige vers la page index.html après la mise à jour du ticket
    return render(request, 'ticket/update_ticket.html', {'form': form, 'ticket': ticket})

def traitement(request):
    lform = TicketForm(request.POST)
    if lform.is_valid():
        ticket = lform.save()
        return render(request, 'ticket/affiche.html', {'Ticket': ticket})
    else:
        return render(request, 'ticket/ajout.html', {'form': lform})
