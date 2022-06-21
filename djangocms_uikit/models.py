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


class UkBasePlugin(CMSPlugin):
    class Meta:
        abstract = True

    extra_classes = models.CharField(max_length=200, null=True, blank=True)


class CardsPluginModel(UkBasePlugin):
    STYLE_CHOICES = (
        ('uk-card-default', 'default'),
        ('uk-card-primary', 'primary'),
        ('uk-card-secondary', 'secondary'),
    )

    SIZE_CHOICES = (
        ('uk-card-small', 'small'),
        ('uk-card-large', 'large')
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    style = models.CharField(choices=STYLE_CHOICES, max_length=20, null=True, blank=True)
    size = models.CharField(choices=SIZE_CHOICES, max_length=20, null=True, blank=True)
    hover = models.BooleanField(default=False)

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


class UkGridModel(UkBasePlugin):
    GUTTER_CHOICES = (
        ('uk-grid-small', _('Small')),
        ('uk-grid-medium', _('Medium')),
        ('uk-grid-large', _('Large')),
        ('uk-grid-collapse', _('Collapse')),
    )
    FLEX_CHOICES = (
        ('uk-flex-left', 'left'),
        ('uk-flex-center', 'center'),
        ('uk-flex-right', 'right'),
        ('uk-flex-between', 'between'),
        ('uk-flex-around', 'around'),
    )

    gutter = models.CharField(choices=GUTTER_CHOICES, max_length=20, default=None, null=True, blank=True)
    divider = models.BooleanField(default=False)
    match = models.BooleanField(default=False, verbose_name=_('Match Height'), )
    masonry = models.BooleanField(default=False)

<<<<<<< HEAD
    grid_gutter = models.CharField(choices=GUTTER_CHOICES, max_length=20, null=True, blank=True)
    grid_divider = models.BooleanField(default=False)
=======
    child_width_expand = models.BooleanField(default=False)
    child_width_expand_s = models.BooleanField(default=False)
    child_width_expand_m = models.BooleanField(default=False)
    child_width_expand_l = models.BooleanField(default=False)
    child_width_expand_xl = models.BooleanField(default=False)
>>>>>>> 1df502bb880bf3ad51d3fbba33c92621dd494039

    flex = models.CharField(max_length=20, choices=FLEX_CHOICES, default=None, blank=True, null=True)

    child_width = models.IntegerField(default=None, null=True, blank=True)
    child_width_s = models.IntegerField(default=None, null=True, blank=True)
    child_width_m = models.IntegerField(default=None, null=True, blank=True)
    child_width_l = models.IntegerField(default=None, null=True, blank=True)
    child_width_xl = models.IntegerField(default=None, null=True, blank=True)


class UkContainerModel(UkBasePlugin):
    container_expand = models.BooleanField(default=False)


class UkAccordionItemModel(UkBasePlugin):
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    open = models.BooleanField(default=False)


class UkAccordionModel(UkBasePlugin):
    collapsible = models.BooleanField(default=False)
    multiple = models.BooleanField(default=True)
    animation = models.BooleanField(default=True)
    active = models.IntegerField(default=None)
    duration = models.IntegerField(default=200)
    transition = models.CharField(choices=TRANSITION_CHOICES, default='ease', max_length=20)


class UkSectionModel(UkBasePlugin):
    STYLE_CHOICES = (
        ('uk-section-default', 'Default'),
        ('uk-section-muted', 'Muted'),
        ('uk-section-primary', 'Primary'),
        ('uk-section-secondary', 'Secondary'),
    )

    style = models.CharField(choices=STYLE_CHOICES, max_length=200, default=None)
