from django.apps import AppConfig


class ProductEntryProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_entry_product'

    def ready(self):
        import product_entry_product.signals.post_save
        import product_entry_product.signals.post_delete
