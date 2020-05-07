# Generated by Django 2.0.7 on 2019-12-17 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.SmallIntegerField(choices=[(0, '未申请打手审核'), (1, '黑铁'), (2, '青铜'), (3, '白银'), (4, '黄金'), (5, '白金'), (6, '钻石'), (7, '超凡大师'), (8, '傲世宗师'), (9, '最强王者')], default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='user',
            name='nice_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='win_point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(default='icon/default.png', upload_to='icon'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
