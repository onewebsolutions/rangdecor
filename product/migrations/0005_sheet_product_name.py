# Generated by Django 3.1 on 2020-12-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201208_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='product_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
