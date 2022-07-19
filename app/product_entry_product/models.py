from django.db import models

from product.models import Product
from product_entry_document.models import EntryDocument


class EntryProduct(models.Model):
    quantity = models.IntegerField(db_column='quantity')
    cost = models.DecimalField(max_length=6, decimal_places=2, db_column='cost')
    entry_document = models.ForeignKey(EntryDocument, db_column='entry_document_id', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)

