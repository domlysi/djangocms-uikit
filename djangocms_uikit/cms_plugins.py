from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from djangocms_uikit.models import CardsPluginModel, UkContainerModel, UkGridModel, UkAccordionModel, \
    UkAccordionItemModel, UkSectionModel


@plugin_pool.register_plugin
class UkContainer(CMSPluginBase):
    model = UkContainerModel
    module = _('Layout')
    name = _('UK Container')

    render_template = "djangocms_uikit/uk-container.html"
    allow_children = True


@plugin_pool.register_plugin
class UkGrid(CMSPluginBase):
    model = UkGridModel
    module = _('Layout')
    name = _('UK Grid')

    render_template = "djangocms_uikit/uk-grid.html"
    allow_children = True


@plugin_pool.register_plugin
class UkCardsPlugin(CMSPluginBase):
    model = CardsPluginModel  # model where plugin data are saved
    module = _("Elements")
    name = _("Card")  # name of the plugin in the interface
    render_template = "djangocms_uikit/uk-cards.html"


@plugin_pool.register_plugin
class UkAccordionItem(CMSPluginBase):
    module = _("Elements")
    model = UkAccordionItemModel
    name = _("Accordion Item")
    render_template = "djangocms_uikit/uk-accordion_items.html"
    parent_classes = ("UkAccordion",)


@plugin_pool.register_plugin
class UkAccordion(CMSPluginBase):
    model = UkAccordionModel
    module = _("Elements")
    name = _("Accordion")
    render_template = "djangocms_uikit/uk-accordion.html"
    allow_children = True
    child_classes = ("UkAccordionItem",)


@plugin_pool.register_plugin
class UkSection(CMSPluginBase):
    module = _("Layout")
    name = _("Section")
    render_template = "djangocms_uikit/uk-section.html"
    allow_children = True
    model = UkSectionModel
