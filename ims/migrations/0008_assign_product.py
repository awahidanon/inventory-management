# Generated by Django 5.0.1 on 2024-01-13 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0007_rename_employees_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign',
            name='product',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='ims.product'),
            preserve_default=False,
        ),
    ]
