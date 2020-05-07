# Generated by Django 2.0.7 on 2019-12-23 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_order_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='down_user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='down_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='up_user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='uo_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
