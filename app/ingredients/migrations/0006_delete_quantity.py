# Generated by Django 2.1.2 on 2018-11-19 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0005_auto_20181119_1338'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quantity',
        ),
    ]