from django.dispatch import receiver
from ephios.core.signals import nav_link


@receiver(
    nav_link,
    dispatch_uid="ephios_resourcemanagement.register_nav_link",
)
def register_nav_link(sender, **kwargs):
    return {
        "Resources": "#"
    }
