# Generated by Django 2.2.4 on 2019-09-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventcyrcle', '0008_post_author2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author2',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001EA1C8E77B8>', max_length=100),
        ),
    ]
