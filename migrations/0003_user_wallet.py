# Generated by Django 3.0 on 2019-12-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0002_date_joined_auto_now_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wallet',
            field=models.PositiveIntegerField(default=0, verbose_name='Credit of user'),
        ),
    ]
