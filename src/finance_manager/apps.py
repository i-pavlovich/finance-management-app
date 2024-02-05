from django.apps import AppConfig


class FinanceManagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "finance_manager"

    def ready(self) -> None:
        import finance_manager.signals  # noqa
