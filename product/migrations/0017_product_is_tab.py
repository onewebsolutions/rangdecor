# Generated by Django 3.1 on 2020-12-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20201219_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_tab',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]