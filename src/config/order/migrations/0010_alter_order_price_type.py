# Generated by Django 4.2.4 on 2023-10-11 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_ordersatus_remove_order_payment_orderpricechange_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price_type',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10),
        ),
    ]