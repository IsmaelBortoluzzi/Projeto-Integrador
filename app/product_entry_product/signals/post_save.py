from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product
from product_entry_product.models import EntryProduct


@receiver(post_save, sender=EntryProduct)
def add_inventory(sender, instance, **kwargs):
    product = Product.objects.filter(id=instance.product.id).first()

    if product is None:
        return

    product.current_inventory += instance.quantity
    product.save()

