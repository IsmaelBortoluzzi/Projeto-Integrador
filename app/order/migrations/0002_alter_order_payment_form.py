# Generated by Django 4.1 on 2022-08-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_form',
            field=models.CharField(db_column='payment_form', max_length=32),
        ),
    ]
