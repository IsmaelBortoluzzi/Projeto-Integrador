from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, db_column='name')
    initials = models.CharField(max_length=16, db_column='initials', default='')  # sigla
    supplier = models.ForeignKey
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'product_brand'
