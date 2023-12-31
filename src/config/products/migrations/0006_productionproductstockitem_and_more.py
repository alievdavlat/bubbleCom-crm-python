# Generated by Django 4.2.5 on 2023-09-24 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productamount_remove_products_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionProductStockItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('defect_amount', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='productionproduct',
            name='items',
        ),
        migrations.RemoveField(
            model_name='productionproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='productionproduct',
            name='production_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productionproductinfo'),
        ),
        migrations.DeleteModel(
            name='ProductAmount',
        ),
        migrations.AddField(
            model_name='productionproductstockitem',
            name='production_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productionproduct'),
        ),
        migrations.AddField(
            model_name='productionproductstockitem',
            name='stock_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.AddField(
            model_name='productionproduct',
            name='stock_products',
            field=models.ManyToManyField(through='products.ProductionProductStockItem', to='products.products'),
        ),
    ]
