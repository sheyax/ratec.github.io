# Generated by Django 2.2.4 on 2019-09-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventcyrcle', '0002_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourevents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('date_of_event', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='events',
        ),
    ]
