# Generated by Django 4.2.4 on 2023-11-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_products_norm_productionproductinfo_norm'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionproduct',
            name='status',
            field=models.BigIntegerField(default=1),
        ),
    ]
