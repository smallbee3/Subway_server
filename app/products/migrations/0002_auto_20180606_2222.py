# Generated by Django 2.0.5 on 2018-06-06 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_maker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='레시피 제작자'),
        ),
        migrations.AddField(
            model_name='product',
            name='vegetables',
            field=models.ManyToManyField(blank=True, to='products.Vegetables', verbose_name='야채'),
        ),
    ]
