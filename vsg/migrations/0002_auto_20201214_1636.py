# Generated by Django 3.1 on 2020-12-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsg',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vsg',
            name='meta_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
