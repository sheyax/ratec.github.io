# Generated by Django 2.2.4 on 2019-09-08 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventcyrcle', '0009_auto_20190908_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author2',
        ),
    ]