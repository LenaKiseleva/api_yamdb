# Generated by Django 3.0.5 on 2021-04-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='PSQO5Y88OT', max_length=10, null=True, verbose_name='Код подтверждения'),
        ),
    ]
