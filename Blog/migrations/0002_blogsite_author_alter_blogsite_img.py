# Generated by Django 4.2.4 on 2023-08-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsite',
            name='author',
            field=models.TextField(default='Suman', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogsite',
            name='img',
            field=models.ImageField(default=True, upload_to='pics'),
        ),
    ]
