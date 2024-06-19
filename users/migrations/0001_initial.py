# Generated by Django 5.0.6 on 2024-06-19 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=130)),
                ('card_number', models.IntegerField()),
                ('balance', models.FloatField(default=0)),
                ('exp_date', models.IntegerField()),
            ],
            options={
                'verbose_name': 'User card',
                'verbose_name_plural': 'User cards',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=120)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='TransferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('card_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_from', to='users.usercardmodel')),
                ('card_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers_to', to='users.usercardmodel')),
            ],
            options={
                'verbose_name': 'Transfer',
                'verbose_name_plural': 'Transfers',
            },
        ),
        migrations.AddField(
            model_name='usercardmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usermodel'),
        ),
    ]
