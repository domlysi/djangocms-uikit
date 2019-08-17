from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from djangocms_uikit.models import CardsPluginModel, UKContainer, UKGrid


@plugin_pool.register_plugin
class UkContainer(CMSPluginBase):
    model = UKContainer
    module = _('UIKit')
    name = _('Container')

    render_template = "djangocms_uikit/container.html"
    allow_children = True


@plugin_pool.register_plugin
class UkGrid(CMSPluginBase):
    model = UKGrid
    module = _('UIKit')
    name = _('Grid')

    render_template = "djangocms_uikit/grid.html"
    allow_children = True


@plugin_pool.register_plugin
class CardsPlugin(CMSPluginBase):
    model = CardsPluginModel  # model where plugin data are saved
    module = _("UIKit")
    name = _("Card")  # name of the plugin in the interface
    render_template = "djangocms_uikit/cards.html"
    allow_children = True

    # parent_classes = [UkGrid, ]

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
