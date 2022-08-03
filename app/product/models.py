from django.db import models

from product_brand.models import Brand
from supplier.models import Supplier


class Product(models.Model):
    name = models.CharField(max_length=256, db_column='name')
    barcode = models.CharField(max_length=65, db_column='barcode', null=True, blank=True)
    selling_price = models.DecimalField(decimal_places=2, max_digits=7, db_column='selling_price')
    brand = models.ForeignKey(Brand, null=True, db_column='brand_id', on_delete=models.SET_NULL)
    product_category = models.CharField(max_length=64, db_column='product_category')  # should be implemented as a ChoiceField
    description = models.TextField(max_length=2048, db_column='description', default='', null=True, blank=True)
    is_active = models.BooleanField(default=False, db_column='is_active')
    profit_margin = models.DecimalField(max_digits=7, decimal_places=2, db_column='profit_margin', default=0.00)
    current_inventory = models.IntegerField(db_column='current_inventory', default=0)
    minimum_inventory = models.IntegerField(db_column='minimum_inventory', default=0)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        indexes = [
            models.Index(fields=['is_active'])
        ]
