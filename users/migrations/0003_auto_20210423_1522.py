# Generated by Django 3.0.5 on 2021-04-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210423_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='e42iapyeQp', max_length=10, null=True, verbose_name='Код подтверждения'),
        ),
    ]