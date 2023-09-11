# Generated by Django 4.1.8 on 2023-09-08 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=60)),
            ],
        ),
    ]
