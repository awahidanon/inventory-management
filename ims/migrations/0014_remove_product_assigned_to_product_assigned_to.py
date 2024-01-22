# Generated by Django 5.0.1 on 2024-01-13 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0013_delete_assign_remove_product_assigned_to_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='product',
            name='assigned_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ims.employee'),
            preserve_default=False,
        ),
    ]