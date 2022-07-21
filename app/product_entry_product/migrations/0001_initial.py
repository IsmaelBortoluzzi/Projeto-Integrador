# Generated by Django 3.2.13 on 2022-07-21 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_entry_document', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(db_column='quantity')),
                ('cost', models.DecimalField(db_column='cost', decimal_places=2, max_digits=7)),
                ('entry_document', models.ForeignKey(db_column='entry_document_id', on_delete=django.db.models.deletion.CASCADE, to='product_entry_document.entrydocument')),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
    ]
