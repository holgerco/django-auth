# Generated by Django 3.0 on 2020-01-28 00:25

import django.contrib.auth.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('CustomAuth', '0006_auto_20191218_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumberUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_verify', models.DateTimeField(blank=True, null=True, verbose_name='verify date')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='join date')),
                ('is_active', models.BooleanField(default=True, verbose_name='active status')),
                ('is_verify', models.BooleanField(default=False, verbose_name='register status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active.Unselect this instead of deleting accounts.')),
                ('wallet', models.PositiveIntegerField(default=0, verbose_name='Credit of user')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('cellphone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IR', verbose_name='تلفن همراه')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, error_messages={'unique': 'A user with that email already exists.'}, help_text='250 characters or fewer.', max_length=250, null=True, unique=True, verbose_name='ایمیل')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='users', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='users', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
    ]
