# Generated by Django 2.2.4 on 2019-09-03 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventcyrcle', '0005_auto_20190903_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourevents',
            name='organizer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
