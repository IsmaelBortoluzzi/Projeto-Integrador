from django.db import models

from product.models import Product


class ProductIngredients(models.Model):
    quantity = models.IntegerField(db_column='quantity')
    ingredient = models.ForeignKey(Product, db_column='ingredient', related_name='ingredient_set', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, db_column='product', related_name='product_set', on_delete=models.CASCADE)
