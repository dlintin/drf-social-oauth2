# Generated by Django 4.1.7 on 2023-05-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiFactorAuth',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(db_index=True, max_length=255, unique=True)),
                ('backend', models.CharField(max_length=100)),
                ('client_id', models.CharField(max_length=100)),
                ('client_secret', models.CharField(max_length=255)),
                ('code', models.CharField(db_index=True, max_length=6)),
                ('expires', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]