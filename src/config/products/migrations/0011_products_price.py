# Generated by Django 4.2.5 on 2023-10-31 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_currency_productionproduct_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
