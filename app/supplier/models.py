from django.db import models
import datetime


class Supplier(models.Model):
    corporate_name = models.CharField(max_length=128, db_column='corporate_name')
    fantasy_name = models.CharField(max_length=128, db_column='fantasy_name', default='')
    created = models.DateField(db_column='created')
    cnpj = models.CharField(max_length=14, db_column='cnpj', unique=True)
    email = models.EmailField(db_column='email', default='')
    phone_number = models.CharField(max_length=32, default='', db_column='phone_number')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.created = datetime.datetime.now()

        super(Supplier, self).save(force_insert, force_update, using, update_fields)