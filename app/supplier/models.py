from django.db import models
from client.models import Address
import datetime


class Supplier(models.Model):
    corporate_name = models.CharField(max_length=128, db_column='corporate_name')
    fantasy_name = models.CharField(max_length=128, db_column='fantasy_name', null=True)
    created = models.DateField(db_column='created')
    cnpj = models.CharField(max_length=14, db_column='cnpj', unique=True)
    email = models.EmailField(db_column='email', default='')
    phone_number = models.CharField(max_length=32, default='', db_column='phone_number')

    def get_address(self):
        address = Address.objects.filter(supplier=self)
        return address

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.created = datetime.datetime.now()
        super(Supplier, self).save(force_insert, force_update, using, update_fields)