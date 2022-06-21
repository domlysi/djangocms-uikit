from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from djangocms_uikit.models import CardsPluginModel, UkContainerModel, UkGridModel, UkAccordionModel, \
    UkAccordionItemModel, UkSectionModel


@plugin_pool.register_plugin
class UkContainer(CMSPluginBase):
<<<<<<< HEAD
    model = UKContainer
    module = _('UIKit')
    name = _('Container')
=======
    model = UkContainerModel
    module = _('Layout')
    name = _('UK Container')
>>>>>>> 1df502bb880bf3ad51d3fbba33c92621dd494039

    render_template = "djangocms_uikit/container.html"
    allow_children = True


@plugin_pool.register_plugin
class UkGrid(CMSPluginBase):
<<<<<<< HEAD
    model = UKGrid
    module = _('UIKit')
    name = _('Grid')
=======
    model = UkGridModel
    module = _('Layout')
    name = _('UK Grid')
>>>>>>> 1df502bb880bf3ad51d3fbba33c92621dd494039

    render_template = "djangocms_uikit/grid.html"
    allow_children = True


@plugin_pool.register_plugin
class UkCardsPlugin(CMSPluginBase):
    model = CardsPluginModel  # model where plugin data are saved
<<<<<<< HEAD
    module = _("UIKit")
    name = _("Card")  # name of the plugin in the interface
    render_template = "djangocms_uikit/cards.html"
    allow_children = True
=======
    module = _("Elements")
    name = _("Card")  # name of the plugin in the interface
    render_template = "djangocms_uikit/uk-cards.html"
>>>>>>> 1df502bb880bf3ad51d3fbba33c92621dd494039


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
