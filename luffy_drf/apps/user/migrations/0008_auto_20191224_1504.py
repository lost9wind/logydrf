# Generated by Django 2.0.7 on 2019-12-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20191223_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='game_id',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='game_password',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
