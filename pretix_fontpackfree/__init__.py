from django.apps import AppConfig


class PluginApp(AppConfig):
    name = 'pretix_fontpackfree'
    verbose_name = 'Fontpack: Free fonts'

    class PretixPluginMeta:
        name = 'Fontpack: Free fonts'
        author = 'Raphael Michel'
        description = 'Pack of free fonts for pretix\' ticket editor'
        visible = False
        version = '1.1.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_fontpackfree.PluginApp'
