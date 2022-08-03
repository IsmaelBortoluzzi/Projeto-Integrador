from django.db import models

from supplier.models import Supplier


class Client(models.Model):
    full_name = models.CharField(max_length=128, db_column='full_name')
    nickname = models.CharField(max_length=128, db_column='nickname', null=True)
    birth_date = models.DateField(db_column='birth_date', null=True)
    cpf = models.CharField(max_length=11, db_column='cpf', unique=True)
    phone_number = models.CharField(max_length=32, default='', db_column='phone_number')

    def get_address(self):
        address = Address.objects.filter(client=self)
        return address

    def __str__(self):
        return f'{self.id}: {self.nickname if self.nickname else self.full_name}'


class Address(models.Model):
    cep = models.CharField(max_length=8, db_column='cep', default='')
    street = models.CharField(max_length=256, db_column='street', default='')
    number = models.IntegerField(db_column='number', null=True)
    district = models.CharField(max_length=256, db_column='district', default='')
    city = models.CharField(max_length=256, db_column='city', default='')
    state = models.CharField(max_length=2, db_column='state', default='')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id', null=True)
    supplier = models.ForeignKey(Supplier, db_column='supplier_id', on_delete=models.CASCADE, null=True)
