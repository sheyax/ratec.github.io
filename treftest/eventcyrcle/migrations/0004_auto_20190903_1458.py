# Generated by Django 2.2.4 on 2019-09-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventcyrcle', '0003_auto_20190903_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourevents',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ourevents',
            name='date_of_event',
            field=models.DateField(max_length=100),
        ),
    ]
