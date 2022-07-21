# Generated by Django 3.2.13 on 2022-07-21 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_number', models.IntegerField(db_column='document_number')),
                ('document_type', models.CharField(db_column='document_type', default='', max_length=64)),
                ('total_value', models.DecimalField(db_column='total_value', decimal_places=2, max_digits=7)),
                ('emission_date', models.DateTimeField(db_column='emission_date')),
                ('db_registration_date', models.DateTimeField(auto_now_add=True, db_column='db_registration_date')),
                ('supplier', models.ForeignKey(db_column='supplier_id', on_delete=django.db.models.deletion.DO_NOTHING, to='supplier.supplier')),
            ],
        ),
    ]