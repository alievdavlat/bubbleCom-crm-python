# Generated by Django 4.2.4 on 2023-10-31 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_productionproduct_currency_and_more'),
        ('order', '0015_rename_ordersatus_orderstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productionproductinfo'),
        ),
    ]