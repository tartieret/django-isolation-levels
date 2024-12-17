import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CountersConfig(AppConfig):
    name = "app.counters"
    verbose_name = _("Counters")

    def ready(self):
        with contextlib.suppress(ImportError):
            import app.counters.signals  # noqa: F401
