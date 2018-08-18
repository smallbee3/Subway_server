# Generated by Django 2.0.5 on 2018-08-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkedRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Bread 이름을 저장합니다.', max_length=100, unique=True)),
                ('image', models.FilePathField(max_length=255)),
                ('image3x', models.FilePathField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'bread',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Cheese 이름을 저장합니다.', max_length=100, unique=True)),
                ('image', models.FilePathField(max_length=255)),
                ('image3x', models.FilePathField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'cheese',
            },
        ),
        migrations.CreateModel(
            name='LikedRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100까지 MainIngredient의 이름을 저장합니다.', max_length=100)),
                ('image', models.FilePathField(max_length=255)),
                ('image3x', models.FilePathField(max_length=255)),
                ('quantity', models.CharField(blank=True, help_text='100자까지 MainIngredient의 quantity를 저장합니다.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='255자까지 Recipe의 이름을 저장합니다.', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Sandwich의 이름을 저장합니다.', max_length=100, unique=True)),
                ('image_left', models.FilePathField(max_length=255, path='sandwich')),
                ('image3x_left', models.FilePathField(max_length=255, path='sandwich')),
                ('image_right', models.FilePathField(max_length=255, path='sandwich')),
                ('image3x_right', models.FilePathField(max_length=255, path='sandwich')),
                ('ordering_num', models.IntegerField(blank=True, null=True)),
                ('category', models.ManyToManyField(to='recipes.Category', verbose_name='카테고리')),
                ('main_ingredient', models.ManyToManyField(blank=True, to='recipes.MainIngredient', verbose_name='구성재료')),
            ],
        ),
        migrations.CreateModel(
            name='Sauces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Sauce의 이름을 저장합니다.', max_length=100, unique=True)),
                ('image', models.FilePathField(max_length=255)),
                ('image3x', models.FilePathField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Toasting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Toasting 이름을 저장합니다.', max_length=100, unique=True)),
                ('image', models.FilePathField(max_length=255)),
                ('image3x', models.FilePathField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Toasting',
            },
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Topping의 이름을 저장합니다.', max_length=100, unique=True)),
                ('image', models.FilePathField(max_length=255)),
                ('image3x', models.FilePathField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vegetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Vegetable의 이름을 저장합니다.', max_length=100, unique=True)),
                ('quantity', models.CharField(choices=[('조금', '조금'), ('보통', '보통'), ('많이', '많이')], default='보통', max_length=2)),
                ('image', models.FilePathField(max_length=255)),
                ('image3x', models.FilePathField(max_length=255)),
            ],
        ),
    ]