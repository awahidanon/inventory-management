# Generated by Django 5.0.1 on 2024-02-23 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'catagories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Seller',
            new_name='seller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Product Name'),
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('assigned_date', models.DateField(auto_now_add=True)),
                ('pro_id', models.PositiveIntegerField(unique=True, verbose_name='Product Id')),
                ('quantity', models.PositiveIntegerField()),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.department')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ims.product')),
            ],
        ),
    ]
