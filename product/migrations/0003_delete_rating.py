# Generated by Django 3.1 on 2021-01-29 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
