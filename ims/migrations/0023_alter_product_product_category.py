# Generated by Django 5.0.1 on 2024-01-20 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0022_assign_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ims.category'),
        ),
    ]
