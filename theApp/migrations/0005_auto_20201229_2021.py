# Generated by Django 2.2.4 on 2020-12-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0004_auto_20201229_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
