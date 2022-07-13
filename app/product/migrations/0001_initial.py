# Generated by Django 3.2.13 on 2022-06-22 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('product_brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=256)),
                ('cost', models.DecimalField(db_column='cost', decimal_places=2, max_digits=7)),
                ('selling_price', models.DecimalField(db_column='selling_price', decimal_places=2, max_digits=7)),
                ('product_category', models.CharField(db_column='product_category', max_length=64)),
                ('weight', models.IntegerField(db_column='weight')),
                ('description', models.TextField(db_column='description', default='', max_length=2048, null=True)),
                ('is_active', models.BooleanField(db_column='is_active', default=False)),
                ('brand', models.ForeignKey(db_column='brand_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_brand.brand')),
                ('supplier', models.ForeignKey(db_column='supplier_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier')),
            ],
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['is_active'], name='product_pro_is_acti_9d034c_idx'),
        ),
    ]