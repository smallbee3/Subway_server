# Generated by Django 2.0.5 on 2018-09-26 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0005_auto_20180926_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='sauces',
            name='calories',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vegetables',
            name='calories',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]