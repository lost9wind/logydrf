# Generated by Django 2.0.7 on 2019-12-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_recharge_trade_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recharge',
            name='creat_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='recharge',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
