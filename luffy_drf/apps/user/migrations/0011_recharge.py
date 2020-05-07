# Generated by Django 2.0.7 on 2019-12-25 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20191224_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('method', models.SmallIntegerField(choices=[(0, '充值'), (1, '取现')], default=0)),
                ('num', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recharge', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
