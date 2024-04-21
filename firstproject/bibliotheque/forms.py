from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class LivreForm(ModelForm):
    class Meta:

        model = models.Livre
        fields = ('titre', 'auteur', 'nombre_page', 'date_parution', 'resume')

        labels = {
            'titre': _('Titre'),
            'auteur': _('Auteur'),
            'nombre_page': _('Nombre de pages'),
            'date_parution': _('Date de parution'),
            'resume': _('Résumé')
        }

