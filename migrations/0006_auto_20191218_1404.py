# Generated by Django 3.0 on 2019-12-18 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0005_auto_20191218_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_register',
        ),
        migrations.AddField(
            model_name='user',
            name='date_verify',
            field=models.DateTimeField(blank=True, null=True, verbose_name='verify date'),
        ),
    ]