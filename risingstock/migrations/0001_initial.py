# Generated by Django 4.0.2 on 2022-03-01 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RisingStock',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('curprice', models.BigIntegerField()),
                ('diff', models.BigIntegerField()),
                ('ratio', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('per', models.FloatField()),
                ('roe', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsOfRisingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('written_at', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risingstock.risingstock')),
            ],
        ),
    ]
