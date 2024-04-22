from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


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