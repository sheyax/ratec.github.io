# Generated by Django 2.2.4 on 2019-09-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventcyrcle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=100)),
            ],
        ),
    ]
