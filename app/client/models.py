from django.db import models


class Address(models.Model):
    cep = models.CharField(max_length=8, db_column='cep', default='')
    street = models.CharField(max_length=256, db_column='street', default='')
    number = models.IntegerField(db_column='number', null=True)
    district = models.CharField(max_length=256, db_column='district', default='')
    city = models.CharField(max_length=256, db_column='city', default='')
    state = models.CharField(max_length=128, db_column='state', default='')


class Client(models.Model):
    first_name = models.CharField(max_length=128, db_column='name')
    nickname = models.CharField(max_length=128, db_column='nickname', null=True)
    birth_date = models.DateField(db_column='birth_date', null=True)
    cpf = models.CharField(max_length=11, db_column='cpf', unique=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=32, default='', db_column='phone_number')
