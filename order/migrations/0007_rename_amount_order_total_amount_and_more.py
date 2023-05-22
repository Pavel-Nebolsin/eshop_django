# Generated by Django 4.2.1 on 2023-05-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_productinorder_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='amount',
            new_name='total_amount',
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=20, null=True, verbose_name='Цена'),
        ),
    ]