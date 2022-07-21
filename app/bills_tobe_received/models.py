import datetime

from django.db import models
from order.models import Order


class BillsToBeReceived(models.Model):
    inclusion_date = models.DateTimeField(db_column='inclusion_date', default=datetime.datetime.now())
    remaining_value = models.DecimalField(max_digits=7, decimal_places=2, db_column='remaining_value')
    order_id = models.ForeignKey(Order, db_column='order_id', on_delete=models.DO_NOTHING)
    # is_open = models.BooleanField(db_column='is_open')
