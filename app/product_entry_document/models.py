from django.db import models

from supplier.models import Supplier


class EntryDocument(models.Model):
    document_number = models.IntegerField(db_column='document_number')
    document_type = models.CharField(max_length=64, db_column='document_type', default='')
    total_value = models.DecimalField(max_digits=7, decimal_places=2, db_column='total_value')
    emission_date = models.DateTimeField(db_column='emission_date')
    db_registration_date = models.DateTimeField(auto_now_add=True, db_column='db_registration_date')
    supplier = models.ForeignKey(Supplier, db_column='supplier_id', on_delete=models.DO_NOTHING)