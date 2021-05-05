# Generated by Django 3.0.5 on 2021-05-05 09:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210505_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default=uuid.UUID('76175474-ad82-11eb-b2b5-6d315d54747d'), max_length=100, null=True, verbose_name='Код подтверждения'),
        ),
    ]