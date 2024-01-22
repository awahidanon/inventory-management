# Generated by Django 5.0.1 on 2024-01-13 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0014_remove_product_assigned_to_product_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.employee'),
        ),
    ]