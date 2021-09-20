# Generated by Django 3.2.7 on 2021-09-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='Электронная почта')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Админ?')),
                ('activation_code', models.CharField(blank=True, max_length=8, verbose_name='Код активации')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
