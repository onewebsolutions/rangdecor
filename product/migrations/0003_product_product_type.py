# Generated by Django 3.1 on 2020-12-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_finish'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]