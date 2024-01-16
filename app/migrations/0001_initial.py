# Generated by Django 5.0.1 on 2024-01-16 18:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название рецепта')),
                ('description', models.TextField(verbose_name='Описание рецепта')),
                ('preview_image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('time_minutes', models.IntegerField(default=1, help_text='В минутах', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления')),
                ('category', models.CharField(choices=[('B', 'Завтрак'), ('D', 'Обед'), ('S', 'Ужин')], max_length=1, verbose_name='Прием пищи')),
                ('ingredients', models.ManyToManyField(to='app.ingredient', verbose_name='Ингредиенты')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
