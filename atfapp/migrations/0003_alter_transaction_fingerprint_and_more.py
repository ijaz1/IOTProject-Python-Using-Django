# Generated by Django 4.0.1 on 2022-01-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atfapp', '0002_alter_transaction_photo_alter_userdetails_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='fingerprint',
            field=models.ImageField(upload_to='t_fingerprint_img'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='photo',
            field=models.ImageField(upload_to='t_face_image'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='fingerprint',
            field=models.ImageField(upload_to='fingerprint_img'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='photo',
            field=models.ImageField(upload_to='face_image'),
        ),
    ]