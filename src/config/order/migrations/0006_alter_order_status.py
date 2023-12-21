# Generated by Django 4.2.4 on 2023-09-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Being delivered'), (3, 'Delivered')], default=1),
        ),
    ]
