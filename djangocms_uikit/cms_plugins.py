from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from djangocms_uikit.models import CardsPluginModel, UKContainer, UKGrid


@plugin_pool.register_plugin
class UkContainer(CMSPluginBase):
    model = UKContainer
    module = _('Layout')
    name = _('UK Container')

    render_template = "djangocms_uikit/uk-container.html"
    allow_children = True


@plugin_pool.register_plugin
class UkGrid(CMSPluginBase):
    model = UKGrid
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
