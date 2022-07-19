from django.db import models

from product_entry_document.models import EntryDocument


class BillsToBePaid(models.Model):
    bill_type = models.CharField(max_length=64, db_column='bill_type', default='')
    installment_number = models.IntegerField(db_column='installment_number')
    installment_value = models.DecimalField(max_length=6, decimal_places=2, db_column='installment_value')
    due_date = models.DateField(db_column='due_date')
    is_paid = models.BooleanField(db_column='is_paid', default=False)
    entry_document = models.ForeignKey(EntryDocument, db_column='entry_document_id', on_delete=models.CASCADE)
