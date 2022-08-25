from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

from order.models import Order
from product.models import Product


class ProductOutput(models.Model):
    sold_price = models.DecimalField(decimal_places=2, max_digits=7, default=1, db_column='sold_price', validators=[MinValueValidator(Decimal('0.01'))])
    quantity = models.IntegerField(db_column='quantity', default=1, validators=[MinValueValidator(1)])
    product_id = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, db_column='order_id', on_delete=models.DO_NOTHING)

    def sales_total(self):
        return self.quantity * self.sold_price
