# Generated by Django 5.0.1 on 2024-01-13 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0011_rename_seller_product_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='assigned_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ims.employee'),
            preserve_default=False,
        ),
    ]
