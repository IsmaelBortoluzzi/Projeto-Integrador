import datetime

from django.db import models
from order.models import Order


class BillsToBeReceived(models.Model):
    inclusion_date = models.DateField(db_column='inclusion_date', default=datetime.date.today)
    remaining_value = models.DecimalField(max_digits=7, decimal_places=2, default=1.00 ,db_column='remaining_value')
    order_id = models.ForeignKey(Order, db_column='order_id', on_delete=models.DO_NOTHING)