# Generated by Django 5.0 on 2024-02-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_alter_invoice_gst_final_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='new_product_in_frontend',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(),
        ),
    ]
