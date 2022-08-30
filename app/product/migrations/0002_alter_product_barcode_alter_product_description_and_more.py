# Generated by Django 4.1 on 2022-08-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, db_column='barcode', max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, db_column='description', default='', max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(db_column='is_active', default=True),
        ),
    ]