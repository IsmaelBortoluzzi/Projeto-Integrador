from django.apps import AppConfig


class ProductOutputConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_output'

    def ready(self):
        import product_output.signals.post_save