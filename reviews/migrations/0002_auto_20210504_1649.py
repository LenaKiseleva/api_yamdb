# Generated by Django 3.0.5 on 2021-05-04 16:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Минимальная оценка 1'), django.core.validators.MaxValueValidator(10, message='Максимальная оценка 10')], verbose_name='Оценка'),
        ),
    ]
