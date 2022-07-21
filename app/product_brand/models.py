from django.db import models

from supplier.models import Supplier


class Brand(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    initials = models.CharField(max_length=16, db_column='initials', default='')  # sigla

    class Meta:
        db_table = 'product_brand'

    def __str__(self):
        return f'{self.initials} ({self.name})'
