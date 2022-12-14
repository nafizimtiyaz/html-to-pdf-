# Generated by Django 3.1.4 on 2022-11-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('present', models.TextField(blank=True, max_length=300)),
            ],
        ),
    ]
