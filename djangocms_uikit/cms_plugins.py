from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from djangocms_uikit.models import CardsPluginModel, UKContainerModel, UKGridModel, UkAccordionModel, \
    UkAccordionItemModel


@plugin_pool.register_plugin
class UkContainer(CMSPluginBase):
    model = UKContainerModel
    module = _('Layout')
    name = _('UK Container')

    render_template = "djangocms_uikit/uk-container.html"
    allow_children = True


@plugin_pool.register_plugin
class UkGrid(CMSPluginBase):
    model = UKGridModel
    module = _('Layout')
    name = _('UK Grid')

    render_template = "djangocms_uikit/uk-grid.html"
    allow_children = True


@plugin_pool.register_plugin
class CardsPlugin(CMSPluginBase):
    model = CardsPluginModel  # model where plugin data are saved
    module = _("Elements")
    name = _("Cards Plugin")  # name of the plugin in the interface
    render_template = "djangocms_uikit/cards.html"

    # parent_classes = [UkGrid, ]

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class UkAccordionItem(CMSPluginBase):
    module = _("Elements")
    model = UkAccordionItemModel
    name = _("Accordion Item")
    render_template = "djangocms_uikit/accordion_items.html"
    parent_classes = ("UkAccordion",)


@plugin_pool.register_plugin
class UkAccordion(CMSPluginBase):
    model = UkAccordionModel
    module = _("Elements")
    name = _("Accordion")
    render_template = "djangocms_uikit/accordion.html"
    allow_children = True
    child_classes = ("UkAccordionItem",)
