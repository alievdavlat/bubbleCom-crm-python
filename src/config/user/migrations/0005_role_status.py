# Generated by Django 4.2.4 on 2023-09-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_roleaccess_slug_role_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
