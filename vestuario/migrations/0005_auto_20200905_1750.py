# Generated by Django 3.1 on 2020-09-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vestuario', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='adresa',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='broj_telefona',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prezime',
            field=models.CharField(default='', max_length=300),
        ),
    ]
