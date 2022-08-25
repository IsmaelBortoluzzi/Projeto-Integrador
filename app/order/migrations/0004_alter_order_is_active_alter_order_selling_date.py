# Generated by Django 4.1 on 2022-08-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_payment_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(blank=True, db_column='is_active', default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='selling_date',
            field=models.DateField(db_column='selling_date'),
        ),
    ]
