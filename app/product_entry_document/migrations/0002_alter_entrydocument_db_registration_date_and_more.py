# Generated by Django 4.1 on 2022-08-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_entry_document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrydocument',
            name='db_registration_date',
            field=models.DateField(auto_now_add=True, db_column='db_registration_date'),
        ),
        migrations.AlterField(
            model_name='entrydocument',
            name='emission_date',
            field=models.DateField(db_column='emission_date'),
        ),
    ]
