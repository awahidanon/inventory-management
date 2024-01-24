# Generated by Django 5.0.1 on 2024-01-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0024_alter_assign_product_alter_product_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
        migrations.AlterField(
            model_name='assign',
            name='pro_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='Product Id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Product Name'),
        ),
    ]