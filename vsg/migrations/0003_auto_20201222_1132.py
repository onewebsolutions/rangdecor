# Generated by Django 3.1 on 2020-12-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsg', '0002_auto_20201214_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsg',
            name='area_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vsg',
            name='is_show',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
