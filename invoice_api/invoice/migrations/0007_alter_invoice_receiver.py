# Generated by Django 5.0 on 2024-02-13 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_companies_user'),
        ('invoice', '0006_alter_product_properties_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.companies'),
        ),
    ]
