# Generated by Django 3.0.5 on 2021-10-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0009_auto_20211008_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='This page is really awesome...', max_length=300),
        ),
    ]
