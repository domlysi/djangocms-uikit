from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext as _


class CardsPluginModel(CMSPlugin):
    title = models.CharField(max_length=100)
    text = models.TextField()

    badge_value = models.CharField(max_length=100, null=True, blank=True)

    head_title = models.CharField(max_length=100, null=True, blank=True)
    hover = models.BooleanField(default=False)

    STYLE_CHOICES = (
        ('uk-card-default', _('Default')),
        ('uk-card-primary', _('Primary')),
        ('uk-card-secondary', _('Secondary')),
    )
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, default=STYLE_CHOICES[0][0])

    MEDIA_POSITION_CHOICES = (
        ('uk-card-media-top', 'Top'),
        ('uk-card-media-bottom', 'Bottom'),
        ('uk-card-media-left', 'Left'),
        ('uk-card-media-right', 'Right'),
    )
    media = models.ImageField(upload_to="cards/images/", null=True, blank=True)
    media_position = models.CharField(max_length=50, choices=MEDIA_POSITION_CHOICES, null=True, blank=True)

    SIZE_CHOICES = (
        ('uk-card-large', 'Large'),
        ('uk-card-small', 'Small'),
    )
    size = models.CharField(max_length=20, null=True, blank=True, choices=SIZE_CHOICES)


class UKGrid(CMSPlugin):
    GUTTER_CHOICES = (
        ('uk-grid-small', _('Small')),
        ('uk-grid-medium', _('Medium')),
        ('uk-grid-large', _('Large')),
        ('uk-grid-collapse', _('Collapse')),
    )

    grid_gutter = models.CharField(choices=GUTTER_CHOICES, max_length=20, null=True, blank=True)
    grid_divider = models.BooleanField(default=False)

    grid_match = models.BooleanField(default=False, verbose_name=_('Match Height'), )


class UKContainer(CMSPlugin):
    container_expand = models.BooleanField(default=False)
