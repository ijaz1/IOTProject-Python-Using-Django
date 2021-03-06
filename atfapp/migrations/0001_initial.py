# Generated by Django 4.0.1 on 2022-01-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
                ('CurrentDate', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
    ]
