# Generated by Django 4.2.4 on 2023-09-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_delivery_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]