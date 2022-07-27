from django.db import models

from product.models import Product
from product_entry_document.models import EntryDocument

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class EntryProduct(models.Model):
    quantity = models.IntegerField(db_column='quantity')
    cost = models.DecimalField(max_digits=7, decimal_places=2, db_column='cost')
    entry_document = models.ForeignKey(EntryDocument, db_column='entry_document_id', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)

