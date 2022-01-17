# Generated by Django 4.0.1 on 2022-01-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atfapp', '0006_delete_transaction_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.ImageField(upload_to='fingerprint_img')),
                ('photo', models.ImageField(upload_to='face_image')),
                ('CurrentDate', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.ImageField(upload_to='fingerprint_img')),
                ('photo', models.ImageField(upload_to='face_image')),
            ],
        ),
    ]
