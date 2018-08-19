# Generated by Django 2.0.5 on 2018-08-19 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandwich',
            name='calories',
            field=models.SmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='protein',
            field=models.SmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='saturated_fat',
            field=models.SmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='serving_size',
            field=models.SmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='sodium',
            field=models.SmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='sugars',
            field=models.SmallIntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]