# Generated by Django 3.0 on 2019-12-09 15:08

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_register', models.DateTimeField(blank=True, null=True, verbose_name='register date')),
                ('date_joined', models.DateTimeField(blank=True, null=True, verbose_name='join date')),
                ('is_active', models.BooleanField(default=True, verbose_name='active status')),
                ('is_register', models.BooleanField(default=False, verbose_name='register status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active.Unselect this instead of deleting accounts.')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='first name')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, help_text='Required, 250 characters or fewer.', max_length=250, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='users', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='users', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
    ]