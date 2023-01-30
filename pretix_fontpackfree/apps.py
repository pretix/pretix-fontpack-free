from django.apps import AppConfig
from . import __version__
        compatibility = "pretix>=4.16.0"


class PluginApp(AppConfig):
    name = 'pretix_fontpackfree'
    verbose_name = 'Fontpack: Free fonts'

    class PretixPluginMeta:
        name = 'Fontpack: Free fonts'
        author = 'Raphael Michel'
        description = 'Pack of free fonts for pretix\' ticket editor'
        visible = False
        version = __version__
        compatibility = "pretix>=4.16.0"

    def ready(self):
        from . import signals  # NOQA

