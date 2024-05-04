from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class TicketForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ('title', 'description', 'author', 'status', 'category')

        labels = {
            'title': _('Titre'),
            'description': _('Description'),
            'author': _('Auteur'),
            'status': _('Statut'),
            'category': _('Catégorie'),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = models.Category
        fields = ('name', 'description', 'priority')
        labels = {
            'name': 'Nom',
            'description': 'Description',
            'priority': 'Priorité',
        }
        
class TicketIdForm(forms.Form):
    ticket_id = forms.IntegerField(label='ID du ticket')
    actions = (
        ('read_ticket', 'Lire'),
        ('delete_ticket', 'Supprimer'),
        ('update_ticket', 'Modifier'),
    )
    action = forms.ChoiceField(choices=actions, label='Action')
    
class CategoryIdForm(forms.Form):
    category_id = forms.IntegerField(label='ID de la catégorie')
    actions = (
        ('read_category', 'Lire'),
        ('delete_category', 'Supprimer'),
        ('update_category', 'Modifier'),
    )
    action = forms.ChoiceField(choices=actions, label='Action')