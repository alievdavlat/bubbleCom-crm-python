# Generated by Django 4.2.5 on 2023-09-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
