from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms



class TicketForm(ModelForm):
    ### This class is a form that will be used to create a new ticket
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
    ### This class is a form that will be used to create a new category
    priority_choices = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )
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