# Generated by Django 3.2.13 on 2022-06-22 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
        ('product_brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='supplier',
            field=models.ForeignKey(db_column='supplier_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier'),
        ),
    ]
