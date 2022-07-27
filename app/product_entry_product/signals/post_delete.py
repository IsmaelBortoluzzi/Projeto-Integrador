from django.db.models.signals import post_delete
from django.dispatch import receiver

from product.models import Product
from product_entry_product.models import EntryProduct


@receiver(post_delete, sender=EntryProduct)
def subtract_inventory(sender, instance, **kwargs):
    product = Product.objects.filter(id=instance.product.id).first()

    if product is None:
        return

    quantity_to_subtract = product.current_inventory - instance.quantity

    if quantity_to_subtract < product.minimum_inventory:
        return

    product.current_inventory = quantity_to_subtract
    product.save()
