# Generated by Django 5.0.1 on 2024-01-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='calories',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Калорийность'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание ингредиента'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название ингредиента'),
        ),
    ]