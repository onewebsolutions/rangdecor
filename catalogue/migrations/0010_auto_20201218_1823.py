# Generated by Django 3.1 on 2020-12-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20201218_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue_page',
            name='main_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='catalogue'),
        ),
        migrations.AlterField(
            model_name='catalogue_page',
            name='main_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='catalogue'),
        ),
    ]