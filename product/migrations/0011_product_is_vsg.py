# Generated by Django 3.1 on 2020-12-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_product_is_vsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_vsg',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
