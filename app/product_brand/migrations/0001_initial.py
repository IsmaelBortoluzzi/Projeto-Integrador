# Generated by Django 3.2.13 on 2022-07-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('initials', models.CharField(db_column='initials', default='', max_length=16)),
            ],
            options={
                'db_table': 'product_brand',
            },
        ),
    ]
