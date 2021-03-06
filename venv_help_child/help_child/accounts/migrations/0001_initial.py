# Generated by Django 3.2.9 on 2022-02-04 08:32

import accounts.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(default='01', error_messages={'unique': 'A user with that username already exists.'}, help_text='ユーザ名は名前をローマ字で入力してください。この項目は必須です。', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(help_text='ログイン時に必須', max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='メールアドレス')),
                ('last_name', models.CharField(max_length=150, verbose_name='姓')),
                ('first_name', models.CharField(max_length=150, verbose_name='名')),
                ('last_name_kana', models.CharField(max_length=150, verbose_name='姓（かな）')),
                ('first_name_kana', models.CharField(max_length=150, verbose_name='名（かな）')),
                ('sex', models.CharField(choices=[('男性', '男性'), ('女性', '女性')], default='男性', max_length=4, verbose_name='性別')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生年月日')),
                ('postal_code', models.CharField(blank=True, max_length=7, null=True, verbose_name='郵便番号（ハイフンなし）')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='住所')),
                ('tel', models.CharField(blank=True, max_length=11, null=True, verbose_name='電話番号（ハイフンなし）')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'ユーザー',
                'db_table': 'custom_user',
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='T002Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': '保護者テーブル',
            },
        ),
        migrations.CreateModel(
            name='T003Childminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': '保育士テーブル',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=150, verbose_name='ユーザ種別')),
            ],
        ),
    ]
