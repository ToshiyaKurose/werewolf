# Generated by Django 4.2.5 on 2023-09-23 12:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='deleted date')),
                ('username', models.CharField(error_messages={'unique': 'そのユーザー名は既に使用されています。'}, help_text='必須。16文字以内。半角英数字と@/./+/-/_のみ。', max_length=16, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='ユーザー名')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('is_staff', models.BooleanField(default=False, verbose_name='管理者')),
                ('is_active', models.BooleanField(default=False, verbose_name='有効')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'ユーザー',
                'verbose_name_plural': 'ユーザー',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
