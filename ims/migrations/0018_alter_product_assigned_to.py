# Generated by Django 5.0.1 on 2024-01-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0017_alter_product_assigned_to_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, default=None, to='ims.employee'),
        ),
    ]
