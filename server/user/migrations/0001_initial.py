# Generated by Django 4.1.4 on 2022-12-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('verified', models.BooleanField(default=0, verbose_name='Email підтверджено')),
                ('name', models.CharField(max_length=255, null=True, verbose_name="Ім'я")),
                ('lname', models.CharField(max_length=255, null=True, verbose_name='Призвище')),
                ('sname', models.CharField(max_length=255, null=True, verbose_name='По батькові')),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Номер телефону')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_admin', models.BooleanField(default=False)),
                ('subscription', models.BooleanField(default=True, verbose_name='Підписати пошту')),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Востаннє в мережі')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата реєстрації')),
                ('device_token', models.CharField(max_length=50, null=True, unique=True)),
                ('notifications', models.BooleanField(default=1)),
                ('fcm_token', models.CharField(max_length=255, null=True)),
                ('update_departaments', models.BooleanField(default=False)),
                ('social_type', models.PositiveIntegerField(choices=[(1, 'fb'), (2, 'g')], null=True)),
                ('social_id', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Користувачи',
                'verbose_name_plural': 'Користувачи',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('image', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PassCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, verbose_name='Код')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
