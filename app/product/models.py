from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, db_column='name')
    cost = models.DecimalField(decimal_places=2, max_digits=7, db_column='cost')
    selling_price = models.DecimalField(decimal_places=2, max_digits=7, db_column='selling_price')
    brand = models.ForeignKey  # TODO fazer a tabela brand
    product_category = models.CharField(max_length=64, db_column='product_category')  # should be implemented as a ChoiceField
    weight = models.IntegerField(db_column='weight')  # weight MUST be in grams
    fornecedor = models.ForeignKey  # TODO fazer a tabela fornecedor
    description = models.TextField(max_length=2048, db_column='description', default='', null=True)
    is_active = models.BooleanField(default=False, db_column='is_active')
