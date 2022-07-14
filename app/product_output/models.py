from django.db import models

from order.models import Order
from product.models import Product


class ProductOutput(models.Model):
    quantity = models.IntegerField(db_column='minimum_inventory', default=0)
    product_id = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)
    product_output_id = models.ForeignKey(Order, db_column='product_output_id', on_delete=models.DO_NOTHING)
