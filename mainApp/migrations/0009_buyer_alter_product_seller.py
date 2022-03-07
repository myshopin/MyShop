# Generated by Django 4.0.1 on 2022-02-13 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_product_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('addressline1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('pic', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller'),
        ),
    ]