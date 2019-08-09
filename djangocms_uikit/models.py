from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext as _

TRANSITION_CHOICES = (
    ('linear', 'linear'),
    ('ease', 'ease'),
    ('ease-in', 'ease-in'),
    ('ease-in-out', 'ease-in-out'),
    ('ease-out', 'ease-out'),
)


class CardsPluginModel(CMSPlugin):
    title = models.CharField(max_length=100)
    text = models.TextField()


class UKGridModel(CMSPlugin):
    GUTTER_CHOICES = (
        ('uk-grid-small', _('Small')),
        ('uk-grid-medium', _('medium')),
        ('uk-grid-large', _('large')),
        ('uk-grid-collapse', _('collapse')),
    )

    grid_gutter = models.CharField(choices=GUTTER_CHOICES, max_length=20)
    grid_divider = models.BooleanField(default=False)

    grid_match = models.BooleanField(default=False, verbose_name=_('Match Height'), )


class UKContainerModel(CMSPlugin):
    container_expand = models.BooleanField(default=False)


class UkAccordionItemModel(CMSPlugin):
    extra_classes = models.CharField(max_length=200, null=True, blank=True)

    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    open = models.BooleanField(default=False)


class UkAccordionModel(CMSPlugin):
    extra_classes = models.CharField(max_length=200, null=True, blank=True)

    collapsible = models.BooleanField(default=False)
    multiple = models.BooleanField(default=True)
    animation = models.BooleanField(default=True)
    active = models.IntegerField(default=None)
    duration = models.IntegerField(default=200)
    transition = models.CharField(choices=TRANSITION_CHOICES, default='ease', max_length=20)
