from django.db import models


class Address(models.Model):
    cep = models.CharField(max_length=8, db_column='cep', default='')
    street = models.CharField(max_length=256, db_column='street', default='')
    number = models.IntegerField(db_column='number', null=True)
    district = models.CharField(max_length=256, db_column='district', default='')
    city = models.CharField(max_length=256, db_column='city', default='')
    state = models.CharField(max_length=2, db_column='state', default='')

