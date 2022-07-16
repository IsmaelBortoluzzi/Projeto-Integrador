from django.db import models

from client.models import Client


class Order(models.Model):
    selling_date = models.DateTimeField(db_column='selling_date')
    payment_form = models.CharField(max_length=32, db_column='payment_form', default='cash')
    is_active = models.BooleanField(default=True, db_column='is_active')
    client_id = models.ForeignKey(Client, db_column='client_id', on_delete=models.DO_NOTHING)
