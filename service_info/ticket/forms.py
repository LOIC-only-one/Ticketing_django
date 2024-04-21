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
