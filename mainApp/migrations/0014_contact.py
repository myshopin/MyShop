# Generated by Django 4.0.1 on 2022-02-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('phone', models.CharField(default=None, max_length=15)),
                ('message', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
