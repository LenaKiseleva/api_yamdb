# Generated by Django 3.0.5 on 2021-07-24 13:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210505_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default=uuid.UUID('e461daac-ec80-11eb-9b4c-c57b7d998622'), max_length=100, null=True, verbose_name='Код подтверждения'),
        ),
    ]
