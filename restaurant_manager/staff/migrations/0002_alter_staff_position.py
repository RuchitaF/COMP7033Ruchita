# Generated by Django 4.0.10 on 2023-05-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(max_length=255),
        ),
    ]
