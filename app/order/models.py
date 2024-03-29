from django.db import models

from client.models import Client


class Order(models.Model):
    selling_date = models.DateField(db_column='selling_date')
    payment_form = models.CharField(max_length=32, db_column='payment_form', default='Dinheiro', null=True)
    is_active = models.BooleanField(default=True, db_column='is_active', blank=True)
    client_id = models.ForeignKey(Client, db_column='client_id', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id}: {f"{self.selling_date}"[:10]} -> {self.client_id}'

    class Meta:
        indexes = [
            models.Index(fields=['is_active'])
        ]