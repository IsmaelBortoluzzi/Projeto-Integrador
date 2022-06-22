from django.db import models

from supplier.models import Supplier


class Brand(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    initials = models.CharField(max_length=16, db_column='initials', default='')  # sigla
    supplier = models.ForeignKey(Supplier, db_column='supplier_id', null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'product_brand'
