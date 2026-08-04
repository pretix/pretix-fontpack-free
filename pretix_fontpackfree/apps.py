from django.apps import AppConfig

from . import __version__


class PluginApp(AppConfig):
    name = "pretix_fontpackfree"
    verbose_name = "Fontpack: Free fonts"

    class PretixPluginMeta:
        name = "Fontpack: Free fonts"
        author = "Raphael Michel"
        description = "Pack of free fonts for pretix"
        visible = False
        version = __version__
        compatibility = "pretix>=2026.8.0.dev0"

    def ready(self):
        from . import signals  # NOQA
