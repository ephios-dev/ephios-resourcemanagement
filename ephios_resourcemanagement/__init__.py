from ephios.core.plugins import PluginConfig


class AppConfig(PluginConfig):
    name = "ephios_resourcemanagement"

    class EphiosPluginMeta:
        name = "ephios_resourcemanagement"
        author = "Ephios Team <team@ephios.de>"
        description = "This plugin lets user manage resources like vehicles and assign them to shifts."

    def ready(self):
        from . import signals  # NOQA


default_app_config = "ephios_resourcemanagement.AppConfig"