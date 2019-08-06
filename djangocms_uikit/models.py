from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext as _


class CardsPluginModel(CMSPlugin):
    title = models.CharField(max_length=100)
    text = models.TextField()


class UKGrid(CMSPlugin):
    GUTTER_CHOICES = (
        ('uk-grid-small', _('Small')),
        ('uk-grid-medium', _('medium')),
        ('uk-grid-large', _('large')),
        ('uk-grid-collapse', _('collapse')),
    )

    grid_gutter = models.CharField(choices=GUTTER_CHOICES, max_length=20)
    grid_divider = models.BooleanField(default=False)

    grid_match = models.BooleanField(default=False, verbose_name=_('Match Height'), )


class UKContainer(CMSPlugin):
    container_expand = models.BooleanField(default=False)
