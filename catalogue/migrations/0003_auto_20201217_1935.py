# Generated by Django 3.1 on 2020-12-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_catalogue_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue_page',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='catalogue/pages'),
        ),
    ]
