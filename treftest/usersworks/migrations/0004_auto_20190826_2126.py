# Generated by Django 2.2.4 on 2019-08-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersworks', '0003_auto_20190826_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
